import os
import json
import datetime
import paho.mqtt.client as mqtt
from flask import Flask, request, render_template
from bson.json_util import dumps
from pymongo import MongoClient, errors

# UPDATE
###################### INIT ##############################
app = Flask(__name__)


###################### CONFIGURATION ##############################
# APP CONFIG OBJECT
config = {
    'app': {
        'title': 'SimpleChat',
        'description': 'Simple chat using Python Flask, MongoDB and Paho MQTT.'
    },
    'mqtt':{
        'roottopic': os.environ['MQTT_ROOT_TOPIC'],
        'broker': os.environ['MQTT_ADDRESS'],
        'port': int(os.environ['MQTT_PORT']),
        'user': os.environ['MQTT_USER'],
        'password': os.environ['MQTT_PASSWORD'],   
    },
    'mongodb': {
        'host': os.environ['MONGODB_HOSTNAME'], 
        'port': 27017, 
        'db': os.environ['MONGODB_DATABASE']
    }
}



###################### MONGO ##############################
# SETUP DB CONNECTION AND MESSAGES COLLECTION
db_connection = MongoClient(
        host = config['mongodb']['host'],
        port = config['mongodb']['port'],
        serverSelectionTimeoutMS = 3000) # 3 second timeout
db = db_connection[config['mongodb']['db']]
messages = db['messages']




###################### MQTT ##############################
# CALLBACKS FUNCTION FOR MQTT CLIENT
def on_message(client, userdata, message):
    # get message, decode it 
    payload = json.loads(message.payload.decode("utf-8"))
    if (payload['username'] and payload['message']):
        # if user and message properties are there insert new message in DB
        msg = {'username': payload['username'], 'message':  payload['message']}
        msg['timestamp'] = datetime.datetime.now().strftime('%a %b %d %Y %H:%M:%S')
        obj = messages.insert_one(msg)
    else:
        # else reply error to MQTT clients
        client.publish('{}/status'.format(config["mqtt"]["roottopic"]),"username or message is missing.") 

#as soon as the client connects successfully, it subscribes to post messages topic
def on_connect(client, userdata, flags, rc):
    print("Connected to " + os.environ['MQTT_ADDRESS'])
    client.subscribe('{}/postmessage'.format(config["mqtt"]["roottopic"]))

# SETUP MQTT CLIENT CONNECTION TO DATABUS
client = mqtt.Client()
#set username and password, must be created it databus configurator
client.username_pw_set(config["mqtt"]["user"], config["mqtt"]["password"])
#add callback functions
client.on_message = on_message
client.on_connect = on_connect



###################### FLASK ##############################
# Home page
@app.route('/')
def index():
    return render_template('index.html', app = config['app'], mqtt = config['mqtt'])

# Refresh chat
@app.route('/messages/json')
def all():
    # LIMIT MAX NUMBER OF MESSAGES, DISPLAY LAST 100
    total = messages.count()
    limit = 100
    if (total > limit):
        skip = total - limit;
        all = messages.find().limit(limit).skip(skip)
    else:
        all = messages.find()

    return dumps(all)

# Add new message
@app.route('/messages/add', methods=['POST'])
def add():
    # GET USER AND MESSAGE FROM FRONTEND
    username = request.form['username']
    message = request.form['message']

    # check if props are regularly passed
    if (username and message):
        # create message row for DB and insert
        msg = {'username': username, 'message': message}
        msg['timestamp'] = datetime.datetime.now().strftime('%a %b %d %Y %H:%M:%S')
        obj = messages.insert_one(msg)

        # and send the JSON msg to MQTT clients
        msg.pop('_id', None) #remove this prop
        client.publish('{}/getmessage'.format(config["mqtt"]["roottopic"]), json.dumps(msg))

        return dumps({'status': 'ok', 'obj': obj.inserted_id})

    return dumps({'status': 'error'})


# Clear chat data
@app.route('/messages/clear', methods=['POST'])
def clear():
    # delete all messages data
    messages.delete_many({})
    
    return dumps({'status': 'ok'})





###################### START ##############################
if __name__ == '__main__':
    # connect MQTT Client and run Flask App
    client.connect(config["mqtt"]["broker"], port=config["mqtt"]["port"])
    client.loop_start()
    app.run(host='0.0.0.0', port=5000, debug=True)
