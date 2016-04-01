from django import forms

from social.apps.django_app.default.models import DjangoStorage as social_data

class UserForm(forms.ModelForm):
	class Meta:
		model = social_data.user
		fields = [
			"extra_data",
		]