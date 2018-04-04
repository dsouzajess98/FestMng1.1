# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Fuser,Request 

# Register your models here.
admin.site.register(Fuser)
admin.site.register(Request)