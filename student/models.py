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


# defining a method to return rollno in string. self similar to this. Blank contains an empty string unlike null. It will create table auto
	def getdept(self):
		if self.dept=='ECC':
			return str(self.dept)
		else:
			return False
		
class Request(models.Model):
	rid = models.IntegerField(unique=True,null=False)
	Type = models.CharField(max_length=255)
	descrp = models.CharField(max_length=255 ,null=True) 
	fromuser =  models.ForeignKey(User, to_field='username',related_name='fromuser', default='james')
	touser = models.ForeignKey(User, to_field='username', related_name='touser', default='admin')
	date = models.DateField(null=True)
	
	def __str__(self) :
	    return str(self.rid)

		
