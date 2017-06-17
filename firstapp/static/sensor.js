$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/sensor/");

    chatsock.onopen = function() {
      // When web socket opens
           $('#sensor').text("Connected!");
            chatsock.send("Here's some text that the server is urgently awaiting!");
    };

    chatsock.onmessage = function(message) {
      // when message arrive
        $('#sensor').text(message.data);
    };

});