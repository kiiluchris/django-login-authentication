from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Profile_Pictures(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name  = models.CharField(max_length=30, null=True)
	def __unicode__(self):
		return self.name