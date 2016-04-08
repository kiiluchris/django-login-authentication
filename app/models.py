from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.
class Profile_Pictures(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name  = models.CharField(max_length=30, null=True)
	def __unicode__(self):
		return self.name
		
class Request(models.Model):
	request  = models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now=True,auto_now_add=False)
	def __unicode__(self):
		return self.request