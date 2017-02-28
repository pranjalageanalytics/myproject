from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
   url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page':'/home/'}),
   url(r'^$', views.Home, name='home'),
   url(r'^gifter/', views.Gifter_login, name='gifter'),
   url(r'^success/', views.success_gifter, name='success'),
      
   url(r'^host/', views.success_host, name='host'),
   url(r'^pagenotfound/', views.errorview, name='errorview'),
   url(r'^challenge/', views.Challenge, name='challenge'),
   url(r'^my_challenge/', views.My_Challenge, name='my_challenge'),
   url(r'^favourite_challenge/', views.Favourite_Challenge, name='favourite_challenge'),
    
   url(r'^my_profile/', views.My_Profile, name='my_profile'),
   url(r'^upload_profile_pic/$', views.UploadProfileImage, name='upload_profile_pic'),

   url(r'^save/$', views.Save, name='save'),
   
   url(r'^host_save/$', views.Host_registration, name='host_save'),
   
   url(r'^gifter_update/$', views.gifter_update, name='gifter_update'),
   url(r'^host_profile/', views.Host_Profile, name='host_profile'),
         
    
   url(r'^location/$', views.location, name='location'),
   url(r'^location_save/$', views.location_save, name='location_save'),

   url(r'^upload_pic', views.picture, name='upload_pic'),
   
   url(r'^category_save/$', views.category_save, name='category_save'),
   
   url(r'^category/$', views.category, name='category'),
   url(r'^logout/$', views.logout, name='logout'),
   url(r'^forget_password/',views.Forget_Password,name='forget_password'),
   
   url(r'^past_challenges/',views.Past_Challenges,name='past_challenges'),
   url(r'^faq/', views.FAQ, name='faq'),
   url(r'^disclaimer/', views.Disclaimer, name='disclaimer'),      
    url(r'^faq_host/', views.FAQ_host, name='faq_host'),
   url(r'^disclaimer_host/', views.Disclaimer_host, name='disclaimer_host'),      
   
   url(r'^reset_password_save/',views.reset_password_save,name='reset_password_save'),
   
   url(r'^my_goal/', views.My_Goal, name='my_goal'), 
   url(r'^set_goal/', views.set_goal, name='set_goal'),
   
   url(r'^joinchallenge/(?P<pk>[0-9]+)$', views.joinchallenge, name='joinchallenge'),  
   url(r'^acceptchallenge/(?P<pk>[0-9]+)$', views.acceptchallenge, name='acceptchallenge'),  
   url(r'^rejectchallenge/(?P<pk>[0-9]+)$', views.rejectchallenge, name='rejectchallenge'),
   url(r'^tentativechallenge/(?P<pk>[0-9]+)$', views.tentativechallenge, name='tentativechallenge'),    
   url(r'^get_participants/(?P<accp_id>[0-9]+)$', views.get_participants, name='get_participants'),
   url(r'^create_challenge/', views.Create_Challenge, name='create_challenge'),
   #url(r'^acceptchallengehost/(?P<pk>[0-9]+)$', views.acceptchallengehost, name='acceptchallengehost'),
   
   url(r'^acceptchallengehost/(?P<pk>[0-9]+)/(?P<challenge_id>[0-9]+)$', views.acceptchallengehost, name='acceptchallengehost'),
   url(r'^rejectchallengehost/(?P<pk>[0-9]+)/(?P<challenge_id>[0-9]+)$', views.rejectchallengehost, name='rejectchallengehost'),
   
   url(r'^host_challenges/', views.host_challenges, name='host_challenges'),
   url(r'^host_status/', views.host_status, name='host_status'),

   url(r'^past_challenges_host/', views.Past_Challenges_Host, name='past_challenges_host'),

   url(r'^host_toggle/', views.host_toggle, name='host_toggle'),
   url(r'^host_toggle_save/', views.host_toggle_save, name='host_toggle_save'),
   url(r'^gifter_toggle/', views.gifter_toggle, name='gifter_toggle'),
   
   url(r'^challenge_update/(?P<pk>[0-9]+)$', views.challenge_update, name='challenge_update'),
   url(r'^favouritechallenge/(?P<pk>[0-9]+)$', views.favouritechallenge, name='favouritechallenge'),
   url(r'^unfavouritechallenge/(?P<pk>[0-9]+)$', views.unfavouritechallenge, name='unfavouritechallenge'),
   url(r'^inbox/', views.gifter_inbox, name='inbox'),  
   url(r'^host_inbox/', views.host_inbox, name='host_inbox'),  
   url(r'^gifter_ranking/', views.gifter_ranking, name='gifter_ranking'),
   url(r'^host_ranking/', views.host_ranking, name='host_ranking'),
  
   url(r'^gifterfeedbackchallenge/(?P<pk>[0-9]+)$', views.gifterfeedbackchallenge, name='gifterfeedbackchallenge'),
   url(r'^hostfeedbackchallenge/(?P<pk>[0-9]+)/(?P<ch_id>[0-9]+)$', views.hostfeedbackchallenge, name='hostfeedbackchallenge'),
   url(r'^getchallengecompletedlist/(?P<accp_id>[0-9]+)$', views.getchallengecompletedlist, name='getchallengecompletedlist'),   
   url(r'^checkhostfeedback/(?P<accp_id>[0-9]+)$', views.checkhostfeedback, name='checkhostfeedback'),
   url(r'^checkgifterfeedback/(?P<ch_id>[0-9]+)/(?P<accp_id>[0-9]+)$', views.checkgifterfeedback, name='checkgifterfeedback'),
   url(r'^category_unselect/', views.category_unselect, name='category_unselect'), 
   url(r'^fblogin/', views.fblogin, name='fblogin'),  
   url(r'^googlelogin/', views.googlelogin, name='googlelogin'),  
   url(r'^reset_password_host/',views.reset_password_host,name='reset_password_host'),
    
     
]