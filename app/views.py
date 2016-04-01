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

@login_required(login_url='/')
def social_user_profile(request, id = None):
	sUser = get_object_or_404(UserSocialAuth, id = id)
	
	print(sUser.user)
	context = {
		"first_name": user,
	}
	return render(request, "test.html", context)



def logout(request):
    auth_logout(request)
    return redirect('/')