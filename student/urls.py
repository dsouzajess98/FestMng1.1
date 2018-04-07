from django.conf.urls import url
from . import views

urlpatterns = [
	
    url(r'^home/(?P<param1>[A-Za-z0-9.-_]+)/$', views.home),  #param1 is the parameter type of values that acceptable + means more than one character[0-9](6). it is mandatory to send url
	url(r'^savereq/$',views.savereq),
	url(r'^savereq/(?P<par>[A-Za-z0-9.,]+)/$',views.savereq),
	url(r'^signin/$',views.signin),
	url(r'^index/$',views.home,name="index"),
	url(r'^index/callmeet/$',views.callameet,name="meet"),
	url(r'^savemeet/$',views.saveameet,name="save"),
	url(r'^index/createrequest/(?P<to>[A-Za-z0-9.,]+)/$',views.newreq),
	url(r'^logout/$',views.logout_view,name="logout"),
	url(r'^createrequest/$',views.newreq,name="createreq"),
	url(r'^newmessage/$',views.newmsg,name="newmsg"),
    url(r'^saveData/$', views.saveData),
	url(r'^myprofile/$', views.prof),
	url(r'^cred/$',views.dispCred),url(r'^profileupd/$',views.profupd),
    url(r'^cred/(?P<id>[A-Za-z0-9.,]+)/$',views.dispCred),
	url(r'^recrequest/$', views.recrequest,name="recreq"),
	url(r'^pendrequest/$', views.pendrequest,name="pendrequest"),
	url(r'^updreq/(?P<req>[A-Za-z0-9.,]+)/$', views.updreq,name="updreq"),
	url(r'^recrequestchk/(?P<req>[A-Za-z0-9.,]+)/$', views.recrequestchk,name="recrequestchk/(?P<req>[A-Za-z0-9.,]+)"),
	#url(r'^pendrequestchk/(?P<req>[A-Za-z0-9.,]+)/$', views.pendrequestchk,name="pendrequestchk/(?P<req>[A-Za-z0-9.,]+)"),
]