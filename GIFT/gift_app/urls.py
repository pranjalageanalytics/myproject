
from django.conf.urls import include, url
from .views import CreateLocation,CategoryCreateList,CategoryUpdateRetriveList,UserChallengeCategoryLocation,UserChallengeCategoryLocationRetriveUpdate,\
UserCategoryCreateList,UserLocationCreateList,LocationRetriveUpdateList,ChallengeList,CreateMyChallenge,StatusList,GifterCategoryList,GifterAcceptance,\
UserCategoryUpdate,UserLocationUpdate,HostChallengeList,GifterChallengeList,AcceptGifterChallengewiseByHostList,UserSelectedCategory,SetGoal,GetGoal,\
UpdateGoal,GoalPercentageCalculation,UserSelectedLocation,GifterMyChallenge,UpdateMyChallenge,CreateChallengeImage,GifterMyFavouriteChallenge,\
GifterMyPastChallenge,MakeFavouriteMyChallenge,HostMyPastChallenge,SetHostFeedback,SetGifterFeedback,GetGifterChallengeCompletedList,GetHostRanking,\
GetGifterRanking,GetNotificationInboxForHost,GetNotificationInboxForGifter,GetHostRating,GetGifterRating,CheckHostFeedback,CheckGifterFeedback,GetRewards

from . import views

from rest_framework import routers
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from push_notifications.api.rest_framework import APNSDeviceAuthorizedViewSet



router = routers.DefaultRouter()
router.register(r'usercategories', views.CategoriesCreateViewSet, {'group_id','categories','user_id'})# /?categories=1,2,3
router.register(r'userupdatecategories', views.CategoriesUpdateViewSet, {'group_id','categories','user_id'})# /?categories=2,3
router.register(r'userlocations', views.UserLocationCreateList, {'group_id','locations','user_id'})# /?locations=1,2,3
router.register(r'userupdatelocations', views.UserLocationUpdate, {'group_id','locations','user_id'})# /?locations=2.3
#router.register(r'gifter_acceptance_by_host',views.GifterAcceptance,{'challenge_id','status'},name='go-away')
router.register(r'devices', FCMDeviceAuthorizedViewSet)
router.register(r'device/apns', APNSDeviceAuthorizedViewSet)
urlpatterns = [
    # URLs that do not require a session or valid token
    url(r'^location/$', CreateLocation.as_view()), 
    url(r'^location/(?P<pk>[0-9]+)$', LocationRetriveUpdateList.as_view()),
    url(r'^category/$', CategoryCreateList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)$', CategoryUpdateRetriveList.as_view()),
    
    #url(r'^gifter_category/$', GifterCategoryList.as_view()),
    #url(r'^gifter_category/(?P<pk>[0-9]+)$', UserCategoryUpdate.as_view()),    
    url(r'^user_selected_categories/(?P<user_id>[0-9]+)$', UserSelectedCategory.as_view()),
    url(r'^user_selected_location/(?P<user_id>[0-9]+)$', UserSelectedLocation.as_view()),
    #url(r'^userlocation/(?P<pk>[0-9]+)$', UserLocationUpdate.as_view()),
    
    url(r'^create_challenge/(?P<group_id>[0-9]+)/(?P<user_id>[0-9]+)$', UserChallengeCategoryLocation.as_view()),
    url(r'^update_challenge/(?P<pk>[0-9]+)/(?P<group_id>[0-9]+)$', UserChallengeCategoryLocationRetriveUpdate.as_view()),
    #url(r'^challengelist/(?P<location>.+)/(?P<category>.+)/$', ChallengeList.as_view()),
    url(r'^hostchallenge/(?P<group_id>[0-9]+)/(?P<user_id>[0-9]+)$', HostChallengeList.as_view()), 
    url(r'^create_challenge_image/(?P<pk>[0-9]+)$', CreateChallengeImage.as_view()),    
    url(r'^gifterchallenge/(?P<group_id>[0-9]+)/(?P<user_id>[0-9]+)$', GifterChallengeList.as_view()),    
    url(r'^create_mychallenge/(?P<group_id>[0-9]+)/(?P<challenge_id>[0-9]+)/(?P<user_id>[0-9]+)$', CreateMyChallenge.as_view()),
    url(r'^update_mychallenge/(?P<pk>[0-9]+)$', UpdateMyChallenge.as_view()),
    url(r'^makefavourite/(?P<group_id>[0-9]+)/(?P<challenge_id>[0-9]+)/(?P<user_id>[0-9]+)$', MakeFavouriteMyChallenge.as_view()),
    url(r'^status/$', StatusList.as_view()),   
    url(r'^accept_gifter_list_by_host/(?P<challenge_id>[0-9]+)/(?P<user_id>[0-9]+)$', AcceptGifterChallengewiseByHostList.as_view()),    
    url(r'^gifter_acceptance_by_host/(?P<pk>[0-9]+)/(?P<user_id>[0-9]+)$', GifterAcceptance.as_view()), #(?P<my_challenge>[0-9]+)/
    url(r'^gifter_mychallenge_list/(?P<user_id>[0-9]+)$', GifterMyChallenge.as_view()), 
    url(r'^gifter_myfavouritechallenge_list/(?P<user_id>[0-9]+)$', GifterMyFavouriteChallenge.as_view()), 
    url(r'^gifter_mypastchallenge_list/(?P<user_id>[0-9]+)$', GifterMyPastChallenge.as_view()),
    url(r'^host_pastchallenge_list/(?P<group_id>[0-9]+)/(?P<user_id>[0-9]+)$', HostMyPastChallenge.as_view()), 
    url(r'^setgoal/(?P<user_id>[0-9]+)$', SetGoal.as_view()),    
    url(r'^updategoal/(?P<pk>[0-9]+)$', UpdateGoal.as_view()),    
    url(r'^getgoal/(?P<user_id>[0-9]+)$', GetGoal.as_view()),   
    url(r'^goalpercentage/(?P<user_id>[0-9]+)$', GoalPercentageCalculation.as_view()),
    #gifter gives feedback to host of particular challenge
    url(r'^sethostfeedback/(?P<challenge_id>[0-9]+)/(?P<user_id>[0-9]+)$', SetHostFeedback.as_view()),
    #host gives feedback to gifterwho have completed his particular challenge
    url(r'^getchallengecompletedlist/(?P<challenge_id>[0-9]+)/(?P<user_id>[0-9]+)$', GetGifterChallengeCompletedList.as_view()),
    url(r'^setgifterfeedback/(?P<challenge_id>[0-9]+)/(?P<gifter>[0-9]+)$', SetGifterFeedback.as_view()),
    url(r'^gethostranking/(?P<user_id>[0-9]+)$', GetHostRanking.as_view()), 
    url(r'^getgifterranking/(?P<user_id>[0-9]+)$', GetGifterRanking.as_view()), 
    url(r'^getHostNotification/(?P<user_id>[0-9]+)$', GetNotificationInboxForHost.as_view()), 
    url(r'^getGifterNotification/(?P<user_id>[0-9]+)$', GetNotificationInboxForGifter.as_view()), 
    url(r'^gethostrating/(?P<group_id>[0-9]+)/(?P<user_id>[0-9]+)$', GetHostRating.as_view()),   
    url(r'^getgifterrating/(?P<group_id>[0-9]+)/(?P<user_id>[0-9]+)$', GetGifterRating.as_view()), 
    url(r'^', include(router.urls)),
    url(r'^checkhostfeedback/(?P<challenge_id>[0-9]+)/(?P<user_id>[0-9]+)$', CheckHostFeedback.as_view()),
    url(r'^checkgifterfeedback/(?P<challenge_id>[0-9]+)/(?P<gifter>[0-9]+)$', CheckGifterFeedback.as_view()),
    url(r'^getrewards/(?P<group_id>[0-9]+)/(?P<user_id>[0-9]+)$', GetRewards.as_view()),

    
]
