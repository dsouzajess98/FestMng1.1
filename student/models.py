# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Brmsg(models.Model):
	mid = models.IntegerField(unique=True,null=False)
	msg = models.CharField(max_length=256, null=False, default='Important Message')
	
	def __str__(self) :
	    return str(self.mid)
	
class Fuser(models.Model):

	fid = models.IntegerField(unique=True, null=False, default=1000)

	# max capacity of any field in django is 255. Allows null value
	nop = models.IntegerField(null=False, default=0)
#	un = models.CharField(max_length=256)
	un = models.ForeignKey(User, to_field='username')
	dept = models.CharField(max_length=256, null=False, default='ECC')
	post = models.CharField(max_length=256, null=False, default='Workforce')
	subc = models.ForeignKey(User, to_field='username', related_name='subc', null=True)
	core = models.ForeignKey(User, to_field='username', related_name='core', null=True)
	filter = models.IntegerField(null=False, default=1)

class QCM(models.Model):

	qdept = models.CharField(max_length=256) # inner dept : oc,doc,tre,spons
	quser = models.ForeignKey(User, to_field='username')
	qpost = models.CharField(max_length=256) # subcore/core/wf
	
class Oversee(models.Model):

	fromd = models.CharField(max_length=256, null=False)
	tod = models.CharField(max_length=256, null=False)
	msg = models.CharField(max_length=256)
	link = models.CharField(max_length=256)
	
class Request(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	rid = models.IntegerField(unique=True,null=False)
	Type = models.CharField(max_length=255)
	descrp = models.CharField(max_length=255 ,null=True) 
	fromuser =  models.ForeignKey(User, to_field='username',related_name='fromuser', default='james')
	touser = models.ForeignKey(User, to_field='username', related_name='touser', default='admin')
	date = models.DateField(null=True)
	result= models.CharField(max_length=255 ,null=False, default= "notseen") 
	
	def __str__(self) :
	    return str(self.rid)
class CallMeet(models.Model):
	
	dati = models.DateTimeField(auto_now_add=False)
	cfrom = models.ForeignKey(User, to_field='username')
	cto = models.ForeignKey(User, to_field='username',related_name='cto')
	agen = models.CharField(max_length=256)
	rep = models.CharField(max_length=256, default='blah')
	ven = models.CharField(max_length=256)
