# In consumers.py
from channels import Group

# Connected to websocket.connect
def ws_connect(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    Group('sensor').add(message.reply_channel)
    message.reply_channel.send({                                            # Reply to individual directly
           "text": "You're connected to sensor group :) ",
    })

def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    print("message")
    print("Received!!" + message['text'])

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)