# simplechat-py

A simple chat system using the Flask framework (python) and MongoDB.

Based on GitHub example [https://github.com/luish/simplechat.git]([https://github.com/luish/simplechat.git).

## Requirements

* [Flask](http://github.com/mitsuhiko/flask)
* [PyMongo](https://github.com/mongodb/mongo-python-driver/)
* [paho-mqtt](https://github.com/eclipse/paho.mqtt.python)

## Build

Run:

```docker
docker-compose up -d --build
```

## Configure MQTT

If MQTT Broker parameters has to be changed, set the following environment variables for ```simplechat-py``` service:

- **MQTT_ADDRESS:** Is the name or IP address of the MQTT Broker. For Industrial Edge default value is ```ie_databus```.
- **MQTT_USER:** User that will be authenticated on MQTT Broker. For Industrial Edge remember to set this user in IEDatabus Configurator. Default value is ```simplechat```.
- **MQTT_PASSWORD:** Password for ```MQTT_USER``` variables above. Default value is ```simplechat```.
- **MQTT_ROOT_TOPIC:** The main topic where application publish and receive data. For Industrial Edge remember to set this topic for the same user above in IEDatabus Configurator. Default value is ```simplechat```.
