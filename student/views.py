# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Fuser,Request,Brmsg,QCM
from django.contrib.auth.decorators import login_required,user_passes_test #even after loging in the function only if he is certain user
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from random import randint, choice
from string import ascii_lowercase,digits

register = template.Library()

def saveData(request):

	if request.method == "POST":
		cid = request.POST['spid']
		print(cid)
		
	if Fuser.objects.filter(fid=cid).exists():
		if Fuser.objects.filter(fid=cid,nop=0).exists() :
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
	resp ={}
	current_user = request.user.username
#	current_user = User.get_username()
	
	if Fuser.objects.filter(un=current_user,filter=1).exists():
		flag=False
	else :
		flag=True
	resp['curr']=flag
	resp = dispreqno(request)
	resp['name'] = current_user
	return render(request,'production/index.html',resp)

@login_required(login_url='/signin')	
def dispreqno(request):
	count = 0
	check = {}

	req = {}
	current_user = request.user
	for r in Request.objects.filter(touser=current_user):
		req[count] = {'fruser1':r.fromuser_id,'msg':r.descrp,'rid':r.rid}
		count = count + 1
		
	check['notif'] = count
	check['req'] = req
	return check
	
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
def recrequest(request):
	resp ={}
	current_user = request.user.username
#	current_user = User.get_username()
	
	if Fuser.objects.filter(un=current_user,filter=1).exists():
		flag=False
	else :
		flag=True
	resp['curr']=flag
	resp = dispreqno(request)
	resp['name'] = current_user
	return render(request,'production/recrequest.html',resp)

@login_required(login_url='/signin')	
def recrequestchk(request,req):
	resp ={}
	current_user = request.user.username
#	current_user = User.get_username()
	
	if Fuser.objects.filter(un=current_user,filter=1).exists():
		flag=False
	else :
		flag=True
	resp['curr']=flag
	resp = dispreqno(request)
	resp['name'] = current_user
	r = Request.objects.get(rid = req)
	resp['rid'] = r.rid
	resp['fromuserreq'] = r.fromuser
	resp['msg'] = r.descrp
	return render(request,'production/acrequest.html',resp)
	
@login_required(login_url='/signin')	
def newmsg(request):

	if request.method == "POST":
		msg = request.POST['msg']	
		check = random_no()
		while Brmsg.objects.filter(mid=check):
			check = random_no()
		obj = Brmsg()
		obj.mid = check
		obj.msg = msg
		obj.save()
		
	return render(request,'production/index.html')	
	
@login_required(login_url='/signin')	
def newreq(request, to='xyzab'):
	response ={}
	response = dispreqno(request)
	allUsers = User.objects.all()
	current_user = request.user.username
	response['name'] = current_user
	response['users'] = allUsers
	allFusers = Fuser.objects.all()
	response['allFusers'] = allFusers	
	count = 0
	for r in Request.objects.filter(touser=current_user):
		count = count + 1

	if to == 'xyzab':
		flag=False
	else :
		flag=True
	response['flag']=flag
	response['notif'] = count	
	response['touser']=to
	

	return render(request,'production/request.html',response)
	
	
@register.assignment_tag()
def random_no(length=3) :
		return randint(10**(length-1),(10**(length)-1))

@login_required(login_url='/signin')		
def savereq(request,par):

	if request.method == 'POST' :

		if par == 'xyzab':
			type = request.POST['type']
			descrp = request.POST['message']
			to = request.POST['tousers1[]']
			datereq = request.POST['date']
			check = random_no()
			
			while Request.objects.filter(rid=check):
				check = random_no()
				
			obj = Request()
			obj.touser=to
			obj.rid=check
			obj.Type=type
			obj.descrp=descrp
			obj.fromuser = request.user	
			obj.date = datereq
			obj.save();
		else:
			type = request.POST['type']
			descrp = request.POST['message']
			datereq = request.POST['date']
			check = random_no()
			key=range(3)
			d=""
			p=""
			for i in key:
				d=d+par[i]
				if i!=2 :
					p=p+par[i+3]
		
			if Fuser.objects.filter(un=request.user,dept=d).exists():
				f=True #same dept
			else:
				f=False #diff dept
			
			g=True
			
			if f==True :
			
				curr=Fuser.objects.get(un=request.user)
				if p=='su' :
					to = curr.subc
				elif p=='co' :
					to = curr.core
				else:
					g=False
				
				if g==True:
					
					while Request.objects.filter(rid=check):
						check = random_no()
					obj = Request()
					obj.rid=check
					obj.Type=type
					obj.descrp=descrp
					obj.fromuser = request.user
					obj.touser = to
					obj.date = datereq
					obj.save();
					
			if f==False or g==False:
				
				to = 'admin'
				minw=10
				
				for usr in Fuser.objects.filter(dept=d,post=p):
					count=0
					for r in Request.objects.filter(touser=usr.un):
						count = count + 1
					if count<minw :
						minw=count
						to = usr.un
					else :
						to = 'admin'
				
				print(to)
				
				while Request.objects.filter(rid=check):
					check = random_no()
					
				obj = Request()
				obj.rid=check
				obj.Type=type
				obj.descrp=descrp
				obj.fromuser = request.user
				obj.touser = to
				obj.date = datereq
				obj.save();
				
				if g==True: #diff dept
					 
					if ( d=='log' or d=='des') and Fuser.objects.filter(un=request.user.username, dept='ecc').exists():
						# identify which qcm su to send notification to
						minw=10
						for qrec in QCM.objects.filter(qdept= 'doc',qpost='su'):
							count=0
							for rec in Request.objects.filter(touser=qrec.quser) :
								count = count +1
							if count<minw:
								minw=count
								toq = qrec.quser
							else :
								toq = 'admin'
						print toq
	#				elif d=='des' and fdep.dept='ecc':
						
			
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
 