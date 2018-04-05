# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Fuser( models.Model):

	fid = models.IntegerField(null=True)
	# max capacity of any field in django is 255. Allows null value
	full_name = models.CharField( max_length=255)
	yofstudy = models.CharField(max_length=255)
	nop = models.IntegerField(null=False, default=0)
	un = models.CharField( max_length=255, default="core")
	pw = models.CharField( max_length=255, default="core@xyz")	

# defining a method to return rollno in string. self similar to this. Blank contains an empty string unlike null. It will create table auto
	def __str__(self):
		return str(self.full_name)
		
class Request(models.Model):
	rid = models.IntegerField(null=False)
	Type = models.CharField(max_length=255)
	descrp = models.CharField(max_length=255 ,null=True) 
	fromuser =  models.CharField(max_length=255 ,null=False)
	touser = models.CharField(max_length=255 ,null=False)
	date = models.DateField(null=True)
	
	def __str__(self) :
	    return str(self.rid)

		
