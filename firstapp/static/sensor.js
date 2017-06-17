$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/sensor/");
    // How data is render on the screen -
    // First It will render the data from the python template then the javascript will render it , as below
    chatsock.onopen = function() {
      // When web socket opens
           $('#sensor').text("Connected!");

    };
    // Below one will send the data to the server
    chatsock.send("Here's some text that the server is urgently awaiting!");

    chatsock.onmessage = function(message) {
      // when message arrive
        $('#sensor').text(message.data);
    };

});