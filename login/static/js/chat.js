$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";

    // For running on localhost
    // var chatsock = new WebSocket(ws_scheme + '://' + window.location.host + window.location.pathname);

    // For running on heroku
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + window.location.pathname);


    console.log(ws_scheme + '://' + window.location.host  + window.location.pathname);

    console.log("Start sending messages");


    chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        console.log("Receiving message");
        console.log(data)
        var chat = $("#chat");
        var ele = $('<tr></tr>');

        if(!data.message.trim()==""){
            ele.append(
                $("<td></td>").text(data.timestamp)
            );
            ele.append(
                $("<td></td>").text(data.handle)
            );
            ele.append(
                $("<td></td>").text(data.message)
            );
            
            chat.append(ele);
        }
    };
    $("#chatform").on("submit", function(event) {
        var message = {
            handle: $('#handle').text(),
            message: $('#message').val(),
        }
        console.log("Sending message");
        console.log(message);
        chatsock.send(JSON.stringify(message));
        $("#message").val('').focus();
        return false;
    });
    
});