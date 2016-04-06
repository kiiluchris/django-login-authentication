# from django.http import HttpResponse
# from channels.handler import AsgiHandler

from channels import Group
from channels.sessions import channel_session

# Create your views here.
# def http_consumer(message):
# 	# Standard HttpResponse - To access ASGI path attribute directly
# 	response = HttpResponse("Hoya! You asked for this: %s" % message.content['path'])
# 	# Encode response into message format (ASGI)
# 	for chunk in AsgiHandler.encode_response(response):
# 		message.reply_channel.send(chunk)

# Connected to websocket.connect - connects service
@channel_session
def ws_connect(message):
	# Work out room name from path(ignore slashes)
	room = message.content['path'].strip('/')
	# Save room in session and add us to group
	message.channel_session['room'] = room
	Group("chat-%s" % room).add(message.reply_channel)

# Connected to websocket.receive - allows message receipt
@channel_session
def ws_message(message):
	# ASGI WebSocket packet received and send packet message types
	# Both have text key for textual data
	Group("chat-%s" % message.channel_session['room']).send({
			"text": message['text'],
		})
	print "Sending message"

# Connected to websocket.diconnect - disconnects service
@channel_session
def ws_disconnect(message):
	Group("chat-%s" % message.channel_session['room']).discard(message.reply_channel)
	print "Disconnecting from WebSocket"