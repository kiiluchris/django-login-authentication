from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter

# from config import CONFIG

from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext



# Create your views here.
# authomatic = Authomatic(CONFIG, '4a4406bbba4a977e6eee28f9e8f27103')

def index(request):
	return HttpResponse("""
			Login with <a href = "login/fb">Facebook</a>.<br/>
			Login with <a href = "login/tw">Twitter</a>.<br/>
			<form action = "login/oi">
				<input type = "text name = "id" placeholder = "me.yahoo.com"/>
				<input tpe = "submit" placeholder = "Authentication With OpenID">
			</form>
		""")

def login(request):
    context = RequestContext(request)
    return render(request, 'login.html', context)


@login_required(login_url='/')
def home(request):	
    context = RequestContext(request)
    return render(request, 'home.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/')


# def login(request, provider_name):
	# response = HttpResponse()
	# result = authomatic.login(DjangoAdapter(request, response), provider_name)

	# # Continue if result is received
	# if result:
	# 	response.write('<a href="..">Home</a>')

	# 	if result.error:
	# 		response.write('<h2>Damn that error: {0}</h2>'.format(result.error.message))

	# 	elif result.user:
	# 		# We have a user!
	# 		if not (result.user.name and result.user.id):
	# 			result.user.update

	# 		# Welcome user
	# 		response.write(u'<h1>Hello {0}</h1>'.format(result.user.name))
	# 		response.write(u'<h2>Your id is: {0}</h2>'.format(result.user.id))
	# 		response.write(u'<h2>Your email is: {0}</h2>'.format(result.user.email))

	# 		# User is logged in

	# 		# Accessing user resources
	# 		if result.user.credentials:
	# 			# Different statements for different providers
	# 			if result.provider.name == 'fb':
	# 				response.write('You are logged in with Facebook.<br/>')

	# 				# Accessing 5 most recent statuses
	# 				url = 'https://graph.facebook.com/{0}?fields=feed.limit(5)'
	# 				url = url.format(result.user.id)

	# 				# Accessing protected resources
	# 				access_response = result.provider.access(url)

	# 				# GET function status
	# 				if access_response.status == 200:
	# 					# Parse response
	# 					statuses = access_response.data.get('feed').get('data')
	# 					error = access_response.data.get('error')

	# 					if error:
	# 						response.write(u"If it wasn't for you. Error {}!".format(error))
	# 					elif statuses:
	# 						response.write('Your 5 most recent statuses:<br/>')
	# 						for message in statuses:
	# 							text = message.get('message')
	# 							date = message.get('created_time')

	# 							response.write(u"<h3>{}</h3>".format(text))
	# 							response.write(u"Posted on :{}".format(date))

	# 				else:
	# 					response.write('If only I knew you I could fix you...<br/>')
	# 					response.write(u"Status: {}".format(response.status))

	# 			if result.provider.name == 'tw':
	# 				response.write("You are logged in with Twitter<br/>")

	# 				# 5 most recent tweets
	# 				url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
	# 				# Querying the tweets
	# 				access_response = result.provider.access(url, {'count': 5})

	# 				# Parse response.
	# 				if access_response.status == 200:
	# 					if type(access_response.data) is list:
	# 						# Twitter returns the tweets as a JSON list.
	# 						response.write('Your 5 most recent tweets:')
	# 						for tweet in access_response.data:
	# 							text = tweet.get('text')
	# 							date = tweet.get('created_at')

	# 							response.write(u'<h3>{0}</h3>'.format(text))
	# 							response.write(u'Tweeted on: {0}'.format(date))

	# 					elif response.data.get('errors'):
	# 						response.write(u'Damn that error: {0}!'.\
	# 						format(response.data.get('errors')))
	# 				else:
	# 					response.write('Damn that unknown error!<br />')
	# 					response.write(u'Status: {0}'.format(response.status))
    
	# return response