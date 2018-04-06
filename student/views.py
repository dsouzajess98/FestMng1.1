# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Fuser,Request
from django.contrib.auth.decorators import login_required,user_passes_test #even after loging in the function only if he is certain user
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from random import randint, choice
from string import ascii_lowercase,digits

register = template.Library()
def saveData(request):

	if request.method == "POST":
		cid = request.POST['spid']

	if Fuser.objects.filter(fid=cid).exists():
		if Fuser.objects.filter(nop=0).exists() :
 			return redirect(dispCred,cid)
		else:
			check = {}
			check['msg'] = 1
			check['flag'] = 0
			return render(request, 'login.html',check)
	else:
		text="""<h2> Invalid ID </h2>"""
		check = {}
		check['msg'] = 2
		check['flag'] = 0
		return render(request, 'login.html',check)

def gen_rand_user(length=8,chars=ascii_lowercase+digits,split=4,delimiter='-'):
	check = ''.join([choice(chars) for i in xrange(length)])
	return check
	
def dispCred(request,id):

	if Fuser.objects.filter(fid=id,nop=1).exists():
			text="""<h1> Credentials already issued </h1>"""
			check = {}
			check['msg'] = 1
			check['flag'] = 0

			return render(request, 'login.html',check) 

#			return render(request, 'login.html',check)
	if Fuser.objects.filter(fid=id).exists() == False:
			text="""<h1> Invalid ID </h1>"""
			check = {}
			check['msg'] = 1
			check['flag'] = 0
			return render(request, 'login.html',check)			
			

	obj=Fuser.objects.filter(fid=id)
	
	resp={}
	resp['flag']=1
	resp['msg'] = 0
		
	
	usn = gen_rand_user()
	pw = gen_rand_user()
	
	resp['username']=usn
	print(pw)
	while User.objects.filter(username=resp['username']):
		resp['username'] = gen_rand_user()
	resp['password']=pw
	user = User.objects.create_user(username = usn,password = pw,email='')
	fob=Fuser.objects.filter(fid=id).update(nop=1,un=usn)
	return render(request, 'login.html',resp)


def fourdig(request):
#need to write code to check if first time
	return render(request, 'start.html')
	
	
@login_required(login_url='/signin')	
def home(request):
	response ={}
	current_user = request.user.username
#	current_user = User.get_username()
	response['name'] = current_user
	count = 0 
	for r in Request.objects.filter(touser=current_user):
		count = count + 1
	response['notif'] = count
	if Fuser.objects.filter(un=current_user,filter=1):
		curr=False
	else :
		curr=True
	
	response['curr']=curr
	return render(request,'production/index.html',response)
	#return redirect('\gentelella-master\production\index.html')

@login_required(login_url='/signin')	
def prof(request):
	response ={}
	current_user = request.user.username
#	current_user = User.get_username()
	response['name'] = current_user
	count = 0 
	for r in Request.objects.filter(touser=current_user):
		count = count + 1
	response['notif'] = count
	response['flag']=0
	for u in Fuser.objects.filter(un=current_user):
		if u.nop == 1 :
			fob=Fuser.objects.filter(fid=id).update(nop=2)
			response['flag']=1
			
	return render(request,'production/profile.html',response)
	
@login_required(login_url='/signin')	
def profupd(request):
	return render(request,'production/profile.html',response)
	
@login_required(login_url='/signin')	
def newreq(request, to='xyz'):
	response ={}
	allUsers = User.objects.all()
	current_user = request.user.username
	Fuse= Fuser.objects.filter(un=current_user)
	response['name'] = current_user
	response['users'] = allUsers
	response['fusers']= Fuse
	count = 0
	for r in Request.objects.filter(touser=current_user):
		count = count + 1
	response['notif'] = count
	if(to=='xyz'):
		response['flag']=0
	else:
		response['flag']=1
		
	return render(request,'production/request.html',response)

@register.assignment_tag()
def random_no(length=3) :
		return randint(10**(length-1),(10**(length)-1))
		
def savereq(request):
	if request.method =="POST":
		type = request.POST['type']
		descrp = request.POST['message']
		touser = request.POST['to']
		datereq = request.POST['date']
		print(type)
		check = random_no()
		while Request.objects.filter(rid=check):
			check = random_no()
		obj = Request()
		obj.rid=check
		obj.Type=type
		obj.descrp=descrp
		current_user=request.user.username
		obj.fromuser=current_user
		obj.touser = touser
		obj.date = datereq
		obj.save();
		
			
	return redirect('/index')	
	
	
def signin(request):
	response = {}
	if request.method == 'POST' :
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is None :
			return render(request,'login.html',response)
		else :
			login(request,user)
			return redirect('/index')
	return render(request,'login.html',response) #simply pressed login with no details redirect bakc
		
def logout_view(request):
    logout(request)
    return render(request,'login.html')		
 