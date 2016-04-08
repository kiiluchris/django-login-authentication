from django import forms

from social.apps.django_app.default.models import DjangoStorage as social_data

from .models import Request

class UserForm(forms.ModelForm):
	class Meta:
		model = social_data.user
		fields = [
			"extra_data",
		]
		
class RequestForm(forms.ModelForm):
	class Meta:
		model = Request
		fields = [
			"request",
			]