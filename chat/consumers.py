from django.http import HttpResponse

from channels.handler import AsgiHandler
# Create your views here.
def http_consumer(message):
	# Standard HttpResponse - To access ASGI path attribute directly
	response = HttpResponse("Hoya! You asked for this: %s" % message.content['path'])
	# Encode response into message format (ASGI)
	for chunk in AsgiHandler.encode_response(response):
		message.reply_channel.send(chunk)