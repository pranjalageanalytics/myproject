from django.conf.urls import url, include
from django.contrib import admin
from . import views
import notifications.urls

app_name = 'mygift'

urlpatterns = [
               
               url(r'^login/$', views.Login, name='login'),
               url(r'^loginform/$', views.loginform, name='loginform'),
               url(r'^host/$', views.host, name='host'),
               url(r'^challenge/$', views.challenge, name='challenge'),
               url(r'^inbox/notifications/', include(notifications.urls, namespace='notifications')),
               url(r'^hostapprove/$', views.hostapprove, name='hostapprove'),
               url(r'^challengeapprove/$', views.challengeapprove, name='challengeapprove'),
               url(r'^hostreject/$', views.hostreject, name='hostreject'),
               url(r'^challengereject/$', views.challengereject, name='challengereject'),
               url(r'^viewchallenge/$', views.viewchallenge, name='viewchallenge'),
               url(r'^rejectChallenge/$', views.rejectChallenge, name='rejectChallenge'),
               url(r'^approveChallenge/$', views.approveChallenge, name='approveChallenge'),
               url(r'^viewhost/$', views.viewhost, name='viewhost'),
               url(r'^rejectHost/$', views.rejectHost, name='rejectHost'),
               url(r'^approveHost/$', views.approveHost, name='approveHost'),
               url(r'^hostname/$', views.hostname, name='hostname'),
               url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page':'/mygift/login'}),
               url(r'^gifter/$', views.gifter, name='gift'),
               url(r'^viewgift/$', views.viewgift, name='viewgift'),
               url(r'^table/$', views.table_notification, name='table'),
               url(r'^viewnotification/$', views.viewnotification, name='viewnotification'),
               url(r'^mark_as_read/$', views.mark_as_read, name='mark_as_read'),
	       url(r'^notification/$', views.notification,name='notification'),
               
                  
                 
               
               ]

