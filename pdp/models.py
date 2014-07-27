from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Skill(models.Model):
	category = models.CharField(max_length = 30)
	sub_category = models.TextField()

class Mentor(models.Model):
	user = models.OneToOneField(User)
#	id = models.AutoField(primary_key=True)
	approved = models.BooleanField(default = True)
	rating = models.PositiveIntegerField(default = 0, validators = [MaxValueValidator(10), MinValueValidator(100)])
	mentor_skills = models.ManyToManyField(Skill)
	city = models.CharField(max_length = 30, blank = True)
	state = models.CharField(max_length = 30, blank = True)
	skype_id = models.CharField(max_length = 30, blank = True)
	fb_id = models.CharField(max_length = 100, blank = True)

	def __unicode__(self):
		return self.user.username


class Mentee(models.Model):
	user = models.OneToOneField(User)
	mentee_skills = models.ManyToManyField(Skill)
	city = models.CharField(max_length = 30, blank = True)
	state = models.CharField(max_length = 30, blank = True) 
	skype_id = models.CharField(max_length = 30, blank = True)
	fb_id = models.CharField(max_length = 120, blank = True)	
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
	approval_moderator = models.BooleanField(default = True)
	success = models.BooleanField(default = False)
	mentor = models.ForeignKey('Mentor')
	mentee = models.ForeignKey('Mentee')
	start_date = models.DateField(auto_now = True)

