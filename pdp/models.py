from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Skills(models.Model):
	category_list = (
		('tech','Technology'),
		('eng_speak','English speaking'),
		)
	category = models.CharField(max_length = 30, choices = category_list, default = 'Select a category')
	sub_category = models.TextField()

class Mentor(User):
#	user = models.OneToOneField(User)
	id = models.AutoField(primary_key=True)
	approved = models.BooleanField(default = False)
	rating = models.PositiveIntegerField(default = 0, validators = [MaxValueValidator(10), MinValueValidator(100)])
	mentor_skills = models.ManyToManyField(Skills)
	city = models.CharField(max_length = 30)
	state = models.CharField(max_length = 30) 

	def __unicode__(self):
		return self.user.username


class Mentee(models.Model):
	user = models.OneToOneField(User)
	mentor_skills = models.ManyToManyField(Skills)
	city = models.CharField(max_length = 30)
	state = models.CharField(max_length = 30) 
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

class PDP(models.Model):
	approval_mentor = models.BooleanField(default = False)
	approval_moderator = models.BooleanField(default = False)
	success = models.BooleanField(default = False)
	mentor = models.ForeignKey('Mentor')
	mentee = models.ForeignKey('Mentee')
	start_date = models.DateField(auto_now = True)

