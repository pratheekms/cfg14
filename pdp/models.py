from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Mentor(models.Model):
	user = models.OneToOneField(User)
	approved = models.BooleanField(default = False)
	rating = models.PositiveIntegerField(default = 0, validators = [MaxValueValidator(10), MinValueValidator(100)])
	# add additional fields if required

	def __unicode__(self):
		return self.user.username


class Mentee(models.Model):
	user = models.OneToOneField(User)
	# add additional fields if required

	def __unicode__(self):
		return self.user.username

class Moderator(models.Model):
	user = models.OneToOneField(User)
	# add additional fields if required

	def __unicode__(self):
		return self.user.username


class Admin(models.Model):
	user = models.OneToOneField(User)
	# add additional fields if required

	def __unicode__(self):
		return self.user.username

class Skills(models.Model):
	category_list = (
		('tech','Technology'),
		('eng_speak','English speaking'),
		)
	category = models.CharField(max_length = 30, choices = category_list, default = 'Select a category')
	sub_category = models.TextField()