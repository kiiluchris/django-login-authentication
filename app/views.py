from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter

# from config import CONFIG

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext

from django.contrib.auth.models import User

from django.template import Context, Template

from .forms import UserForm

from .pipeline import update_user_social_data as user_data

from social.apps.django_app.default.models import UserSocialAuth

import ast
import unicodedata
import simplejson



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
    return render(request, 'login.html')


@login_required(login_url='/')
def home(request):	
    return render(request, 'home.html')

@login_required(login_url='/')
def social_user_profile(request):
	sUser = UserSocialAuth.objects.get(user= request.user)

	profile_picture = sUser.extra_data['picture_url']

	context = {
		'profile_picture': profile_picture,
		
		}
	
	
	return render(request, "test.html", context)



def logout(request):
    auth_logout(request)
    return redirect('/')