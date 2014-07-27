from django.shortcuts import render_to_response, redirect,render
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from pdp import models
from django.views.decorators.csrf import csrf_exempt

def is_mentor(user):
	return user.groups.filter(name = 'mentors')

def is_mentee(user):
	print user.groups.filter(name = 'mentees')
	return user.groups.filter(name = 'mentees')

def is_moderator(user):
	return user.__class__ == 'Moderator'

def is_admin(user):
	return user.__class__ == 'Admin'

@csrf_exempt
def search(request):
	context = RequestContext(request)
	print "test"
	if(request.method == 'POST'):
		#if(search in request.keys()):
		search_query = request.POST['search']
		print search_query
		mentors = User.objects.filter(username__contains='search_query')
		#else:
		#	mentors = User.objects.all()
			#return render_to_response("search.html", {}, context)
		
		temp = []
		for m in  mentors.all():
			try:
				print m
				a = [m.username, m.mentor.category, m.mentor.sub_category]
				temp.append(m.mentor)
			except:
				a = [m.username, m.username, m.username]
				temp.append(a)
				pass

		print "temp----------------------------------",temp
		return render_to_response("search.html", {'mentors': temp}, context)

	temp = []
	mentors = User.objects.all()
	print mentors
	for m in  mentors.all():
		try:
			a = [m.username, m.mentor.category, m.mentor.sub_category]
			if(len(a) == 3):
				temp.append(m.mentor)
		except:
			pass

	print temp
	return render_to_response("search.html", {'mentors': temp, 'category':category}, context)



#FIXME
def check_pdp(user, context):
	pdp = models.PDP.objects.filter(mentee=user.mentee)
	print pdp
	if(len(pdp) == 1):
		return render_to_response('search.html',{'pdp': pdp, 'user_mentee':user}, context)
	#else:
	temp = []
	mentors = User.objects.all()
	print mentors
	a = []
	for m in  mentors.all():
		try:
			a.append( [m.username])# m.mentor.category, m.mentor.sub_category])
			#temp.append(m.mentor)
		except:
			pass

	print "aaaaaaa", a
	#return render_to_response("search.html",{'mentors': a}, context)
	return redirect('pdp.views.search')






###########################################################

@csrf_exempt
def login(request):
	context = RequestContext(request)
	return render_to_response("login.html")

	if(request.method == 'POST'):
		username = request.POST['InputUsername']
		password = request.POST['InputPassword']
		user = authenticate(username=username, password=password)
		if user:
			#if user.is_active:
			auth_login(request, user)
			if(is_mentor(user)):
				return render_to_response("mentordashboard.html", {'mentor':user}, context)
			elif(is_mentee(user)):
				check_pdp(user,context)
			elif(is_moderator):
				return redirect('pdp.views.moderator_dashboard')
			elif(is_admin):
				return redirect('pdp.views.admin_dashboard')
		else:
			return render_to_response("login.html", {}, context)
	elif(request.method == 'GET'):
		return render_to_response("login.html")
	return render_to_response("login.html")
	#return render_to_response("login.html", {}, context)

@csrf_exempt
def loginconfirm(request):
	context = RequestContext(request)
	print request.method, 'loginconfirm'
	if(request.method == "POST"):
		username = request.POST['InputUsername']
		password = request.POST['InputPassword']
		user = authenticate(username=username, password=password)
		if user:
			#if user.is_active:
			auth_login(request, user)
			if(is_mentor(user)):
				return render_to_response("mentordashboard.html", {'mentor':user}, context)
			elif(is_mentee(user)):
				check_pdp(user,context)
			elif(is_moderator):
				return redirect('pdp.views.moderator_dashboard')
			elif(is_admin):
				return redirect('pdp.views.admin_dashboard')
		else:
			return render_to_response("login.html", {}, context)
	print 'get in loginconfirm'
	return render_to_response("search.html", {}, context)

@csrf_exempt
def register_mentor(request):
	context = RequestContext(request)

@csrf_exempt
def mentor_dashboard(request):
	context = RequestContext(request)
	return render_to_response("mentordashboard.html", {}, context)

@csrf_exempt
def mentee_dashboard(request):
	context = RequestContext(request)
	return render_to_response("search.html", {}, context)

@csrf_exempt
def moderator_dashboard(request):
	return HttpResponse("Moderator dashboard")


@csrf_exempt
def admin_dashboard(request):
	return HttpResponse("admin dashboard")

@csrf_exempt
def checklist(request):
	context = RequestContext(request)
	return render_to_response("checklist.html",{}, context)


@csrf_exempt
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
				mentor.save()
				if request.POST.get('personal', True):
					skill = models.Skill(category = 'Personal Development', sub_category = reg_form['InputMessage'])
					skill.save()
					mentor.mentor_skills.add(skill)
				if request.POST.get('learning', True):
					skill = models.Skill(category = 'Learning', sub_category = reg_form['InputMessage'])
					skill.save()
					mentor.mentor_skills.add(skill)
				if request.POST.get('job', True):
					skill = models.Skill(category = 'Job', sub_category = reg_form['InputMessage'])
					skill.save()
					mentor.mentor_skills.add(skill)
				mentor.save()
				g = Group.objects.get(name='mentors') 
				g.user_set.add(user)
				return render_to_response("login.html", {}, context)
							
			elif(reg_form['ment'] == 'mentee'):
				mentee = models.Mentee(user = user,skype_id = reg_form['SkypeId'], fb_id = reg_form['FbId'], state = reg_form['InputState'], city = reg_form['InputCity'])
				mentee.save()
				if request.POST.get('personal', True):
					skill = models.Skill(category = 'Personal Development', sub_category = reg_form['InputMessage'])
					skill.save()
					mentee.mentee_skills.add(skill)
				if request.POST.get('learning', True):
					skill = models.Skill(category = 'Learning', sub_category = reg_form['InputMessage'])
					skill.save()
					mentee.mentee_skills.add(skill)
				if request.POST.get('job', True):
					skill = models.Skill(category = 'Job', sub_category = reg_form['InputMessage'])
					skill.save()
					mentee.mentee_skills.add(skill)
				mentee.save()
				g = Group.objects.get(name='mentees') 
				g.user_set.add(user)
				return render_to_response("login.html", {}, context)

			registered = True
		else:
			wrong_data = True
			render_to_response('register.html',{ 'registered': registered,'wrong_data' : wrong_data }, context)
			
	else:
		render_to_response('register.html', {'registered': registered,'wrong_data' : wrong_data }, context)

	return render_to_response('register.html', {'registered': registered,'wrong_data' : wrong_data }, context)