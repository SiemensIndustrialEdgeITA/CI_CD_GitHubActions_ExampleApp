$(document).ready(function(){

    target = $('.messages');
    refresh(target);

    $('form#add-message').submit(function(){
        $.post('/messages/add', $(this).serialize(), 'json');
        $(this).children('#message').val('').focus();
        refresh(target);
        return false;
    });

    $('form#clear-message').submit(function(){
        $.post("/messages/clear", function(data) {
            alert( "Message Board cleared." );
          });
        refresh(target);
        return false;
    });


    setInterval(function(){
        refresh(target);
    }, 2000);

    function refresh(target){
        $.get('/messages/json', function(data){
            console.log(data)
            list = '<ul>';
            $.each(data, function(i, message){
                console.log()
                list += '<li><i>' + message.timestamp + ' </i><strong>' + message.username + '</strong>: ' + message.message + '</li>';
            });
            list += '</ul>';

            target.html(list);

            // scroll to the end of the chat div
            target.scrollTop(target[0].scrollHeight);

        }, 'json');
    }

})