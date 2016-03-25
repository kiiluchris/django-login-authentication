from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter

from config import CONFIG

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
authomatic = Authomatic(CONFIG, "The clown is eternal, everlasting, undying.")

def home(request):
	return HttpResponse("""
			Login with <a href = "login/fb">Facebook</a>.<br/>
			Login with <a href = "login/tw">Twitter</a>.<br/>
			<form action = "login/oi">
				<input type = "text name = "id" value = "me.yahoo.com"/>
				<input tpe = "submit" value = "Authentication With OpenID">
			</form>
		""")