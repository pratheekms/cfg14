from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from pdp import models

def is_mentor(user):
	return user.groups.filter(name = 'mentors')

def is_mentee(user):
	return user.groups.filter(name = 'mentees')

def is_moderator(user):
	return user.__class__ == 'Moderator'

def is_admin(user):
	return user.__class__ == 'Admin'

#FIXME
def check_pdp(user):
	return HttpResponse("mentee page")





###########################################################


def login(request):
	context = RequestContext(request)

	if(request.method == 'POST'):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user:
			if user.is_active:
				auth_login(request, user)
				if(is_mentor(user)):
					return redirect('pdp.views.mentor_dashboard')
				elif(is_mentee(user)):
					check_pdp(user)
				elif(is_moderator):
					return redirect('pdp.views.moderator_dashboard')
				elif(is_admin):
					return redirect('pdp.views.admin_dashboard')
		else:
			return HttpResponse("Invalid login details.")
	else:
		return render_to_response("login.html", {}, context)

def register_mentor(request):
	context = RequestContext(request)


def mentor_dashboard(request):
	return HttpResponse("Mentor dashboard")


def mentee_dashboard(request):
	return HttpResponse("Mentee dashboard. will be changed")


def moderator_dashboard(request):
	return HttpResponse("Moderator dashboard")


def admin_dashboard(request):
	return HttpResponse("admin dashboard")


def register(request):
	context = RequestContext(request)
	registered = False
	wrong_data = False

	if (request.method == 'POST'):
		reg_form = request.POST

		if (reg_form['InputPassword'] == reg_form['InputConfirmPassword']):
			
			user = User.objects.create_user(username=reg_form['InputUsername'], email=reg_form['InputEmail'],first_name = reg_form['InputFirstName'], last_name = reg_form['InputLastName'], password = reg_form['InputPassword'] )

			if(reg_form['ment'] == 'mentor'):
				mentor = models.Mentor(user = user, approved = False, rating = 0, skype_id = reg_form['SkypeId'], fb_id = reg_form['FbId'], state = reg_form['InputState'], city = reg_form['InputCity'])
				categories = request.POST.getlist('category')
				for category in categories:
					skill = Skills(category = category, sub_category = reg_form['InputMessage'])
					skill.save()
					mentor.mentor_skills.add(skill)
				mentor.save()
				g = Group.objects.get(name='mentors') 
				g.user_set.add(user)
				return redirect('pdp.views.mentor_dashboard')
							
			elif(reg_form['ment'] == 'mentee'):
				mentee = models.Mentee(user = user,skype_id = reg_form['SkypeId'], fb_id = reg_form['FbId'], state = reg_form['InputState'], city = reg_form['InputCity'])
				mentee = mentee.save()
				for category in categories:
					skill = Skills(category = category, sub_category = reg_form['InputMessage'])
					skill.save()
					mentee.mentee_skills.add(skill)
				mentee.save()
				g = Group.objects.get(name='mentees') 
				g.user_set.add(user)
				return redirect('pdp.views.mentee_dashboard')

			registered = True
		else:
			print reg_form, reg_form.errors
			wrong_data = True
			render_to_response('register.html',{ 'registered': registered,'wrong_data' : wrong_data }, context)
			
	else:
		render_to_response('register.html', {'registered': registered,'wrong_data' : wrong_data }, context)

	return render_to_response('register.html', {'registered': registered,'wrong_data' : wrong_data }, context)