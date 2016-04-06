# from django.http import HttpResponse
# from channels.handler import AsgiHandler

from channels import Group

# Create your views here.
# def http_consumer(message):
# 	# Standard HttpResponse - To access ASGI path attribute directly
# 	response = HttpResponse("Hoya! You asked for this: %s" % message.content['path'])
# 	# Encode response into message format (ASGI)
# 	for chunk in AsgiHandler.encode_response(response):
# 		message.reply_channel.send(chunk)

# Connected to websocket.connect - connects service
def ws_add(message):
	Group("chat").add(message.reply_channel)

# Connected to websocket.receive - allows message receipt
def ws_message(message):
	# ASGI WebSocket packet received and send packet message types
	# Both have text key for textual data
	Group("chat").send({
			"text": "[user] %s" % message.content['text']
		})

# Connected to websocket.diconnect - disconnects service
def ws_disconnect(message):
	Group("chat").discard(message.reply_channel)