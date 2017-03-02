from __future__ import division
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import viewsets
# Create your views here.
from task import *
from django.db.models import F
from rest_framework.exceptions import *
import itertools
from .serializers import LocationSerializer,CategoryTypeSerializer,UserChallengeCategoryLocationRelRelSerializer,UserChallengeCategoryLocation_RetriveUpdateSerializer,\
UserCategoryCreateSerializer,UserLocationCreateSerializer,CreateMyChallengeSerializer,StatusSerializer,UserCategorySerializer,\
UserCategoryUpdateSerializer,MyChallengeSerializer,SetGoalSerializer,GetGoalSerializer,UpdateGoalSerializer,GoalSerializer,UserChallengeCategoryLocationListSerializer,\
MyChallengeListSerializer,GifterAcceptanceSerializer,GifterMyChallengeSerializer,UpdateMyChallengeSerializer,UpdateChallengeImageSerializer,MakeMyFavouriteMyChallengeSerializer,\
HostFeedbackSerializer,GifterFeedbackSerializer,HostRankingSerializer,GifterRankingSerializer,NotificationSerializer,GifterRatingSerializer,HostRatingSerializer,GetGoalPercentageSerializer,\
RewardSerializer

from rest_framework.exceptions import APIException
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import TokenAuthentication
from .models import LocationType,CategoryType,UserChallengeCategoryLocationRelRel,UserCategoryRel,UserLocationRel,CategoryLocationRel,MyChallengeRelRel,\
GiftUserType,StatusType,GiftergoalType,UserType,AuthUserGroups,ChallengeType,UserChallengeCategoryLocationRelRelLocation,UserChallengeCategoryLocationRelRelCategory,\
HostFeedback,GifterFeedback,HostRanking,GifterRanking,HostRating,HostRating,GifterRating,NotificationInbox,Reward

from django.contrib.auth.models import User,Group
from fcm_django.models import FCMDevice
from django.db.models import Q
 
 
 
class CreateChallengeImage(generics.RetrieveUpdateAPIView):
    queryset = UserChallengeCategoryLocationRelRel.objects.all() 
    serializer_class= UpdateChallengeImageSerializer

 
""" web service to retrive & update location according to particular instance"""  
class LocationRetriveUpdateList(generics.RetrieveUpdateAPIView):
    serializer_class = LocationSerializer  
    queryset=LocationType.objects.all()
 
class CreateLocation(generics.ListCreateAPIView): 
    serializer_class = LocationSerializer  
    queryset=LocationType.objects.all().order_by('city')
    authentication_classes = (TokenAuthentication,)
    #get_pastchallenge.delay()
 
""" web service to create  category """  
class CategoryCreateList(generics.ListCreateAPIView):
    serializer_class = CategoryTypeSerializer
    queryset=  CategoryType.objects.all().order_by('category_name')  
    authentication_classes = (TokenAuthentication,)
 
""" web service to retrive & update category according to particular instance"""  
class CategoryUpdateRetriveList(generics.RetrieveUpdateAPIView):
    serializer_class = CategoryTypeSerializer
    queryset=  CategoryType.objects.all()
     
"""web service to create challenge by host"""
class UserChallengeCategoryLocation(generics.CreateAPIView):
    serializer_class=UserChallengeCategoryLocationRelRelSerializer    
    queryset=  UserChallengeCategoryLocationRelRel.objects.all()
   # parser_classes = (MultiPartParser, FormParser,JSONParser)
    authentication_classes = (TokenAuthentication,)
    def get_serializer_context(self):
        return {"group_id": self.kwargs['group_id'],"request":self.kwargs['user_id']} 
 
"""web service to retrive & update challenge by host"""  
class UserChallengeCategoryLocationRetriveUpdate(generics.RetrieveUpdateAPIView):
    serializer_class=UserChallengeCategoryLocation_RetriveUpdateSerializer    
    queryset=  UserChallengeCategoryLocationRelRel.objects.all()
    authentication_classes = (TokenAuthentication,)
    def get_serializer_context(self):
        #print self.request.user
        return {"group_id": self.kwargs['group_id']} 
 
"""web service to save user category relation for gifter""" 
class UserCategoryCreateList(generics.ListCreateAPIView):
    serializer_class=UserCategoryCreateSerializer
    queryset=UserCategoryRel.objects.all()
     
     
class UserCategoryUpdate(generics.RetrieveUpdateAPIView):
    serializer_class=UserCategoryUpdateSerializer
    queryset=UserCategoryRel.objects.all()
     
class StatusList(generics.ListAPIView):
    serializer_class=StatusSerializer
    queryset=StatusType.objects.all()
 
 
class CreateMyChallenge(generics.CreateAPIView): 
    serializer_class= CreateMyChallengeSerializer 
    queryset=MyChallengeRelRel.objects.all() 
    authentication_classes = (TokenAuthentication,)
    def get_serializer_context(self):
        print "within view",self.kwargs['user_id']
        return {"group_id": self.kwargs['group_id'],"request":self.kwargs['user_id'],"challenge_id":self.kwargs['challenge_id']}  
       
    
  
 
class GifterCategoryList(generics.ListAPIView):
    serializer_class=UserCategorySerializer
    def get_queryset(self):
        user=self.request.user
        print user.pk
        gifter_user= GiftUserType.objects.filter(user= user.pk)
        if gifter_user:
            print "gifter_user",gifter_user
            user_category=UserCategoryRel.objects.filter(user=gifter_user)
            return user_category
        else:
            message = { "Invalid User" }
            content = {'message':message}
            return Response(content)
         
     
"""web service to get User_Challenges according to location & category"""
class ChallengeList(generics.ListAPIView):
    serializer_class=UserChallengeCategoryLocationRelRelSerializer
    queryset = UserChallengeCategoryLocationRelRel.objects.all()
    def get_queryset(self):
        category_location=CategoryLocationRel.objects.filter(location=self.kwargs['location'],category=self.kwargs['category'])
        if category_location:        
            return self.queryset.filter(category_location__in=[c.pk for c in category_location])
   
class HostChallengeList(generics.ListAPIView): 
    serializer_class=UserChallengeCategoryLocationListSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.request.user
        print user.pk
        group_id=self.kwargs['group_id']
        if group_id=='1':
            usertype= UserType.objects.filter(user= self.kwargs['user_id'])
            authuser=AuthUserGroups.objects.filter(user=usertype[0].user,group=Group.objects.get(pk=1))
            print authuser
            if authuser:
                queryset=UserChallengeCategoryLocationRelRel.objects.filter(~Q(status=StatusType.objects.get(status='complete')),user=authuser[0].pk).order_by('-challenge__post_date')
               
                return queryset
        else:
            raise APIException("Invalid User")
         
  
class GetRewards(generics.ListAPIView): 
    authentication_classes = (TokenAuthentication,)
    serializer_class=RewardSerializer
    def get_queryset(self):
        group_id=self.kwargs['group_id']
        if group_id=='2':
            usertype= UserType.objects.filter(user= self.kwargs['user_id'])
            authuser=AuthUserGroups.objects.filter(user=usertype[0].user,group=Group.objects.get(pk=2))
            print authuser
            rewardlist=[]
            if authuser:
                queryset=Reward.objects.filter(user=authuser[0].pk)
                if queryset:
                    return queryset
                else:
                    reward=Reward.objects.create(user=authuser[0],rewards_point=0)
                    rewardlist.append(reward)
                    return rewardlist
        else:
            raise APIException("Invalid User")  

       
class UserSelectedCategory(generics.ListCreateAPIView):
    serializer_class=CategoryTypeSerializer 
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.request.user
         
        gift_user= User.objects.filter(pk= self.kwargs['user_id'])
        #print gift_user
        auth_user_groups=AuthUserGroups.objects.filter(user=gift_user[0],group=Group.objects.get(pk=2))
        #print auth_user_groups
        if auth_user_groups:
            category=UserCategoryRel.objects.filter(user=auth_user_groups[0].pk)
            cat=CategoryType.objects.filter(category_id__in=[categories.category.pk for categories in category])
           
         #notifications for android end
            return cat
                        
class UserSelectedLocation(generics.ListCreateAPIView):
    serializer_class=LocationSerializer 
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.request.user
         
        gift_user= User.objects.filter(pk= self.kwargs['user_id'])
        #print gift_user
        auth_user_groups=AuthUserGroups.objects.filter(user=gift_user[0],group=Group.objects.get(pk=2))
        #print auth_user_groups
        if auth_user_groups:
            location=UserLocationRel.objects.filter(user=auth_user_groups[0].pk)
            loc=LocationType.objects.filter(id__in=[locations.location.pk for locations in location])
            print loc
            return loc
 
 
class GifterMyChallenge(generics.ListAPIView):
    #serializer_class=UserChallengeCategoryLocationListSerializer
    serializer_class=GifterMyChallengeSerializer
    authentication_classes = (TokenAuthentication,)
    #queryset = UserChallengeCategoryLocationRelRel.objects.all()
    def get_queryset(self):
        user=self.request.user
         
        gift_user= User.objects.filter(pk= self.kwargs['user_id'])
        #print gift_user
        auth_user_groups=AuthUserGroups.objects.filter(user=gift_user[0].pk,group=Group.objects.get(pk=2))
        #print auth_user_groups
        #final_list=[]
        if auth_user_groups:
            queryset=MyChallengeRelRel.objects.filter(~Q(status=StatusType.objects.get(status='complete')),user=auth_user_groups[0]).order_by('-challenge_join_date')
            """for q in queryset:
                challenge=UserChallengeCategoryLocationRelRel.objects.filter(pk=q.user_challenge_category_location.pk)
                for c in challenge:
                    final_list.append(c)"""
            print queryset
                 
            #[Q(tags__name=c) for c in categories]
            #return self.queryset.filter(pk__in=[c.pk for c in final_list])
            return queryset
        else:
            raise APIException("Invalid User")
 
     
class GifterChallengeList(generics.ListAPIView):
    serializer_class=UserChallengeCategoryLocationListSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.request.user
        
        gift_user= User.objects.filter(pk= self.kwargs['user_id'])
        #print gift_user
        auth_user_groups=AuthUserGroups.objects.filter(user=gift_user[0].pk,group=Group.objects.get(pk=self.kwargs['group_id']))
        #print auth_user_groups
        if auth_user_groups:
            category=UserCategoryRel.objects.filter(user=auth_user_groups[0].pk)
            location=UserLocationRel.objects.filter(user=auth_user_groups[0].pk)
            status=StatusType.objects.get(status='host_approve')
            query= UserChallengeCategoryLocationRelRel.objects.filter(status=status).order_by('-challenge__post_date')
            challenge_list=[]
            for q in query:
                challenge_list.append(q)
            #status=StatusType.objects.get(status="gifter_approve")
            final_list=[]            
            # print category,location
            perfect_match=[]
            challenge_category_location=UserChallengeCategoryLocationRelRelLocation.objects.filter(locationtype__in=[locations.location for locations in location]).values_list('userchallengecategorylocationrelrel', flat=True).distinct()
            abcd=[]
            #print "location before :",challenge_category_location
            for abc in challenge_category_location:
                abcd.append(abc)
            open_slots = UserChallengeCategoryLocationRelRelLocation.objects.all().exclude(locationtype__in=[locations.location for locations in location]).values_list('userchallengecategorylocationrelrel', flat=True).distinct()
            #print "excluded : ",open_slots
            pqrs=[]
            for pqr in open_slots:
                pqrs.append(pqr)
            #print open_slots
            new_slot=list(set(abcd) - set(pqrs))
            #print "perfect : ",new_slot
            #print "challenge : ",challenge_category_location
            #for obj in challenge_category_location:
            perfect_match= UserChallengeCategoryLocationRelRelCategory.objects.filter(categorytype__in=[categories.category for categories in category]).filter(userchallengecategorylocationrelrel__in=new_slot)
            #print "perfect_match : ",perfect_match
            #print "category_location : ",challenge_category_location
            if perfect_match:                     
                category_location_challenge_list=UserChallengeCategoryLocationRelRel.objects.filter(pk__in=[challenge.userchallengecategorylocationrelrel.pk for challenge in perfect_match],status=status)
                #print category_location_challenge_list
                if category_location_challenge_list:
                    for challenge in category_location_challenge_list:
                        final_list.append(challenge)
            very_final_list=[]
            loc_cat=UserChallengeCategoryLocationRelRelLocation.objects.filter(locationtype__in=[locations.location for locations in location]).values_list('userchallengecategorylocationrelrel', flat=True).distinct()
            #for r in loc_cat:
            
            abcd=[]
            for abc in loc_cat:
                abcd.append(abc)
            #print "before : ",abcd
            open_slots = UserChallengeCategoryLocationRelRelLocation.objects.all().exclude(locationtype__in=[locations.location for locations in location]).values_list('userchallengecategorylocationrelrel', flat=True).distinct()
            #print "excluded : ",open_slots
            pqrs=[]
            for pqr in open_slots:
                pqrs.append(pqr)
            #print open_slots
            new_slot=list(set(abcd) - set(pqrs))
            #print "new list : ", new_slot
            """for k in new_slot:
                print k.userchallengecategorylocationrelrel.pk"""
            #print new_slot
            l=UserChallengeCategoryLocationRelRel.objects.filter(pk__in=new_slot)
            #print "l: ",l
            location_challenge_list=UserChallengeCategoryLocationRelRel.objects.filter(pk__in=[challenge.pk for challenge in l],status=status)
            #print "location_challenge_list : ",location_challenge_list
            for challenge in location_challenge_list:
                very_final_list.append(challenge)
                          
            very_final=list(set(very_final_list) - set(final_list))
            #print very_final
            for val in very_final:
                #print "vval",val
                final_list.append(val)
            #print "new_list1 : ",new_list1  
            my_list=list(set(challenge_list) - set(final_list))
            for item in my_list:
                final_list.append(item)
            category_challenge_list=[]                   
            #for c in category:
            category_loc=UserChallengeCategoryLocationRelRelCategory.objects.filter(categorytype__in=[categories.category for categories in category]).values_list('userchallengecategorylocationrelrel', flat=True).distinct()
            abcd=[]
            for abc in category_loc:
                abcd.append(abc)
            print "before category: ",abcd
            open_slots = UserChallengeCategoryLocationRelRelCategory.objects.all().exclude(categorytype__in=[categories.category for categories in category]).values_list('userchallengecategorylocationrelrel', flat=True).distinct()
            print "excluded : ",open_slots
            pqrs=[]
            for pqr in open_slots:
                pqrs.append(pqr)
            #print open_slots
            new_slot=list(set(abcd) - set(pqrs))
            old_slot=list(set(abcd) - set(new_slot))
            print "new list : ", old_slot
            for k in new_slot:
                print k
            #print new_slot
            l=UserChallengeCategoryLocationRelRel.objects.filter(pk__in=new_slot)
            
            for c in l:
                category_challenge_list.append(c)
            new_list=[]
            #for r in category_loc1:
            category_challenge_list=UserChallengeCategoryLocationRelRel.objects.filter(pk__in=[challenge.pk for challenge in l],status=status)
            for challenge in category_challenge_list:
                    new_list.append(challenge)
            ket= list(set(new_list) - set(final_list))
            #print ket
            for k in ket:
                final_list.append(k)
            #print "new_list1: ",new_list1
            #print "final_list: ",final_list
             
   	    my_challenge=MyChallengeRelRel.objects.filter(user=auth_user_groups[0].pk,user_challenge_category_location__in=final_list) 
            my_challenge_list=[]
            for mc in my_challenge:
                userchallenge= UserChallengeCategoryLocationRelRel.objects.filter(pk=mc.user_challenge_category_location.pk)
                for uc in userchallenge:
                    my_challenge_list.append(uc)
            last_list=sorted(set(list(set(final_list) - set(my_challenge_list))), key=lambda x: final_list.index(x))
             
        else:
            raise APIException("Invalid User")
        return last_list   
 
                     
               
         
               
class CategoriesCreateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserCategorySerializer
    authentication_classes = (TokenAuthentication,)
     
    def get_queryset(self):
        categories = self.request.query_params.get('categories', None)
        group_id = self.request.query_params.get('group_id', None)
        user_id = self.request.query_params.get('user_id', None)
        if group_id=='2':
            print categories
            print self.request.user
            print "category: ",categories
            gift_user= UserType.objects.filter(user= user_id)
            authuser=AuthUserGroups.objects.filter(user=gift_user[0].user,group=Group.objects.get(pk=2))
            if authuser:
                c=categories.split(u',')
                list=[]
                for category in c:
                    cat=CategoryType.objects.filter(pk=category)
                    if cat:
                        user_cat_rel=UserCategoryRel.objects.filter(user=authuser[0],category=cat[0])
                     
                        if not user_cat_rel:
                            user_category = UserCategoryRel.objects.create(user=authuser[0],category=cat[0])
                            user_category.save()
                            list.append(user_category)
                        else:
                            list.append(user_cat_rel[0])
                return list 
        else:
            raise APIException("Invalid User")
         
class CategoriesUpdateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserCategorySerializer    
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        categories = self.request.query_params.get('categories', None)
        group_id = self.request.query_params.get('group_id', None) 
        user_id = self.request.query_params.get('user_id', None)
        if group_id=='2':
            print categories
            print self.request.user
            print "category: ",categories
            gift_user= UserType.objects.filter(user= user_id)
            authuser=AuthUserGroups.objects.filter(user=gift_user[0].user,group=Group.objects.get(pk=2))
            if authuser:
                c=categories.split(u',')
                list=[]
                user_cat_rel=UserCategoryRel.objects.filter(user=authuser[0])
                         
                if user_cat_rel:
                    for u in user_cat_rel:
                        u.delete()
                for category in c:
                    cat=CategoryType.objects.filter(pk=category)                          
                    user_category = UserCategoryRel.objects.create(user=authuser[0],category=cat[0])
                    user_category.save()
                    list.append(user_category)
                     
                return list 
        else:
            raise APIException("Invalid User")
     
          
"""web service to save user location relation for gifter"""   
class UserLocationCreateList(viewsets.ModelViewSet):
    serializer_class=UserLocationCreateSerializer
    authentication_classes = (TokenAuthentication,)
    #queryset=UserLocationRel.objects.all()
    def get_queryset(self):
        locations = self.request.query_params.get('locations', None)
        print locations
        group_id = self.request.query_params.get('group_id', None)
        user_id = self.request.query_params.get('user_id', None)
        if group_id=='2':
            print self.request.user
            print "locations: ",locations
            gift_user= UserType.objects.filter(user= user_id)
            authuser=AuthUserGroups.objects.filter(user=gift_user[0].user,group=Group.objects.get(pk=2))
            if authuser:
                l=locations.split(u',')
                list=[]
                for location in l:
                    loc=LocationType.objects.filter(pk=location)
                    if loc:
                        user_loc_rel=UserLocationRel.objects.filter(user=authuser[0],location=loc[0])
                         
                        if not user_loc_rel:
                            user_location = UserLocationRel.objects.create(user=authuser[0],location=loc[0])
                            user_location.save()
                            list.append(user_location)
                        else:
                            list.append(user_loc_rel[0])
                return list 
        else:
            raise APIException("Invalid User")
             
             
class UserLocationUpdate(viewsets.ModelViewSet):
    serializer_class=UserLocationCreateSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        locations = self.request.query_params.get('locations', None)
        group_id = self.request.query_params.get('group_id', None)
        user_id = self.request.query_params.get('user_id', None)
        if group_id=='2':
            print locations
            print self.request.user
            print "locations: ",locations
            gift_user= UserType.objects.filter(user= user_id)
            authuser=AuthUserGroups.objects.filter(user=gift_user[0].user,group=Group.objects.get(pk=2))
            if authuser:
                l=locations.split(u',')
                list=[]
                user_loc_rel=UserLocationRel.objects.filter(user=authuser[0])                  
                if user_loc_rel:
                    for u in user_loc_rel:
                        u.delete()
                for location in l:
                    loc=LocationType.objects.filter(pk=location)                     
                    user_location = UserLocationRel.objects.create(user=authuser[0],location=loc[0])
                    user_location.save()
                    list.append(user_location)               
                return list 
        else:
            raise APIException("Invalid User")
    #queryset=UserLocationRel.objects.all()
     
class SetGoal(generics.ListCreateAPIView):
    
    serializer_class=SetGoalSerializer
    queryset=GiftergoalType.objects.all()
    authentication_classes = (TokenAuthentication,)
    
    def get_serializer_context(self):
        return {"request":self.kwargs['user_id'],} 
 
class UpdateGoal(generics.RetrieveUpdateAPIView):
    serializer_class=UpdateGoalSerializer
    queryset=GiftergoalType.objects.all()
    authentication_classes = (TokenAuthentication,)

class GetGoal(generics.ListAPIView):
    serializer_class=GetGoalSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.kwargs['user_id']
        
        gift_user= AuthUserGroups.objects.filter(user=User.objects.get(pk=user),group=Group.objects.get(pk=2))
        if gift_user:
            getgoal=GiftergoalType.objects.filter(user=gift_user[0])
            """if setgoal:
                for s in setgoal:
                    s.goal_hours=s.goal_hours/60
                    s.completed_hours=s.completed_hours/60
                    list1.append(s)"""
            return getgoal
        else:
            raise APIException("Invalid User")
 
class GoalPercentageCalculation(generics.ListAPIView):
    serializer_class=GetGoalPercentageSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.kwargs['user_id']
        list1=[]
        gift_user= AuthUserGroups.objects.filter(user=User.objects.get(pk=user),group=Group.objects.get(pk=2))
        if gift_user:
            percentage_goal=GiftergoalType.objects.filter(user=gift_user[0])
             
            if percentage_goal:
                for goal in percentage_goal:
                    print "gosl hours ",goal.goal_hours 
                    #print int(goal.completed_hours)/int(goal.goal_hours)
                    #print int(goal.completed_tasks)/int(goal.goal_tasks)
                    if goal.goal_hours==0 :
                        #goal.completed_tasks=(int(goal.completed_tasks)/int(goal.goal_tasks))*100
                        goal.completed_hours=0.0
                    if goal.goal_tasks==0:
                        #goal.completed_hours=(int(goal.completed_hours)/int(goal.goal_hours))*100
                        goal.completed_tasks=0.0
                    if goal.goal_tasks>0:
                        goal.completed_tasks=int((int(goal.completed_tasks)/int(goal.goal_tasks))*100)
                    if goal.goal_hours>0:
                        goal.completed_hours=int((int(goal.completed_hours)/int(goal.goal_hours))*100)
                    #goal.completed_hours=(int(goal.completed_hours)/int(goal.goal_hours))*100
                     
                    print "hours",goal.completed_hours
                    print "tasks",goal.completed_tasks
                    list1.append(goal)
        else:
            raise APIException("Invalid User")              
        return list1
             
class GifterMyFavouriteChallenge(generics.ListAPIView):
    serializer_class=GifterMyChallengeSerializer
    authentication_classes = (TokenAuthentication,)
    #queryset = UserChallengeCategoryLocationRelRel.objects.all()
    def get_queryset(self):
        user=self.kwargs['user_id']         
        gift_user= User.objects.filter(pk= user)
        #print gift_user
        auth_user_groups=AuthUserGroups.objects.filter(user=gift_user[0].pk,group=Group.objects.get(pk=2))
        #print auth_user_groups
        #final_list=[]
        if auth_user_groups:
            queryset=MyChallengeRelRel.objects.filter(user=auth_user_groups[0],is_favourite='1').order_by('-challenge_join_date')
            """for q in queryset:
                challenge=UserChallengeCategoryLocationRelRel.objects.filter(pk=q.user_challenge_category_location.pk)
                for c in challenge:
                    final_list.append(c)"""
            print queryset
                 
            #[Q(tags__name=c) for c in categories]
            #return self.queryset.filter(pk__in=[c.pk for c in final_list])
            return queryset
        else:
            raise APIException("Invalid User")


class HostMyPastChallenge(generics.ListAPIView):
    serializer_class=UserChallengeCategoryLocationListSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.kwargs['user_id']
       # print user.pk
        group_id=self.kwargs['group_id']
        if group_id=='1':
            usertype= UserType.objects.filter(user= user)
            authuser=AuthUserGroups.objects.filter(user=usertype[0].user,group=Group.objects.get(pk=1))
            print authuser
            if authuser:
                queryset=UserChallengeCategoryLocationRelRel.objects.filter(user=authuser[0],status=StatusType.objects.get(status='complete'))
               
                return queryset
        else:
            raise APIException("Invalid User") 
      
        
class GifterMyPastChallenge(generics.ListAPIView):
    serializer_class=GifterMyChallengeSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.kwargs['user_id']      
        gift_user= User.objects.filter(pk= user)
        auth_user_groups=AuthUserGroups.objects.filter(user=gift_user[0].pk,group=Group.objects.get(pk=2))
        if auth_user_groups:
            queryset=MyChallengeRelRel.objects.filter(user=auth_user_groups[0],status=StatusType.objects.get(status="complete")).order_by('-challenge_join_date')
            return queryset
        else:
            raise APIException("Invalid User")
    
class UpdateMyChallenge(generics.RetrieveUpdateAPIView):
    queryset = MyChallengeRelRel.objects.all() 
    serializer_class= UpdateMyChallengeSerializer
    authentication_classes = (TokenAuthentication,)

class MakeFavouriteMyChallenge (generics.CreateAPIView):
    queryset = MyChallengeRelRel.objects.all() 
    serializer_class= MakeMyFavouriteMyChallengeSerializer 
    authentication_classes = (TokenAuthentication,)
    def get_serializer_context(self):
        #print self.request.user
        return {"group_id": self.kwargs['group_id'],"request":self.kwargs['user_id'],"challenge_id":self.kwargs['challenge_id']}  


"""user will send challenge id for which challenge he wants to see gifter list"""    
class AcceptGifterChallengewiseByHostList(generics.ListAPIView): 
    serializer_class= MyChallengeListSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.request.user
        print user.pk
        try:        
            host_user= AuthUserGroups.objects.filter(user=User.objects.get(pk=self.kwargs['user_id']),group=Group.objects.get(pk=1))
            if host_user:
                gifter_status=StatusType.objects.filter(Q(status='gifter_approve'))#(status='gifter_approve',status='edit_approve')
                 
                print self.kwargs['challenge_id'],host_user[0].pk
                user_challege_category_location_queryset=UserChallengeCategoryLocationRelRel.objects.filter(pk=self.kwargs['challenge_id'],user=host_user[0].pk)
                 
                print "user_challege_category_location_queryset",user_challege_category_location_queryset
                if user_challege_category_location_queryset:
                    queryset1=MyChallengeRelRel.objects.filter(user_challenge_category_location=user_challege_category_location_queryset[0].pk,status__in=gifter_status)
                    queryset2=MyChallengeRelRel.objects.filter(user_challenge_category_location=user_challege_category_location_queryset[0].pk,status=StatusType.objects.get(status='host_decline'))
                    queryset3=MyChallengeRelRel.objects.filter(user_challenge_category_location=user_challege_category_location_queryset[0].pk,status=StatusType.objects.get(status='host_approve'))
                    queryset4=MyChallengeRelRel.objects.filter(user_challenge_category_location=user_challege_category_location_queryset[0].pk,status=StatusType.objects.get(status='complete'))
                    final_queryset=[]
                    if queryset1:
                        for q in queryset1:
                            final_queryset.append(q)
                    if queryset2:
                        for q in queryset2:
                            final_queryset.append(q)
                    if queryset3:
                        for q in queryset3:
                            final_queryset.append(q)
                    if queryset4:
                        for q in queryset4:
                            final_queryset.append(q)
                    print final_queryset
                    return final_queryset
            else:
                raise APIException("Invalid User")
        except AuthUserGroups.DoesNotExist:            
            pass
 
 
class GifterAcceptance(generics.RetrieveUpdateAPIView):
    queryset = MyChallengeRelRel.objects.all() 
    serializer_class= GifterAcceptanceSerializer
    authentication_classes = (TokenAuthentication,)
    def get_serializer_context(self):
        #print self.request.user
        return {"gifter": self.kwargs['pk'],"request":self.kwargs['user_id']}


class GetGifterChallengeCompletedList(generics.ListAPIView):  
    serializer_class= MyChallengeListSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.kwargs['user_id']
        print user
                
        host_user= AuthUserGroups.objects.filter(user=User.objects.get(pk=user),group=Group.objects.get(pk=1))
        if host_user:
            gifter_status=StatusType.objects.get(status='complete')     
            print self.kwargs['challenge_id'],host_user[0].pk
            user_challege_category_location_queryset=UserChallengeCategoryLocationRelRel.objects.filter(pk=self.kwargs['challenge_id'],user=host_user[0].pk)     
            print "user_challege_category_location_queryset",user_challege_category_location_queryset
            if user_challege_category_location_queryset:
                queryset1=MyChallengeRelRel.objects.filter(user_challenge_category_location=user_challege_category_location_queryset[0].pk,status=gifter_status)
                return queryset1
        else:
            raise APIException("Invalid User")

                
class SetHostFeedback(generics.CreateAPIView):
    queryset = HostFeedback.objects.all() 
    serializer_class= HostFeedbackSerializer
    authentication_classes = (TokenAuthentication,)
    def get_serializer_context(self):
        return {"request":self.kwargs['user_id'],"challenge_id":self.kwargs['challenge_id'],}    
    
    
class SetGifterFeedback(generics.CreateAPIView):
    queryset = GifterFeedback.objects.all() 
    serializer_class= GifterFeedbackSerializer
    authentication_classes = (TokenAuthentication,)
    def get_serializer_context(self):
        return {"gifter":self.kwargs['gifter'],"challenge_id":self.kwargs['challenge_id']}  

class GetHostRanking(generics.ListAPIView):
    serializer_class= HostRankingSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.kwargs['user_id']
        print user
             
        host_user= AuthUserGroups.objects.filter(user=User.objects.get(pk=user),group=Group.objects.get(pk=1))

        if host_user:
            user_challege_category_location_queryset=UserChallengeCategoryLocationRelRel.objects.filter(status=StatusType.objects.get(status='complete'))
            if user_challege_category_location_queryset:
                for challenge in user_challege_category_location_queryset:
                    total_sum=0
                    hostfeedback=HostFeedback.objects.filter(host_user=challenge.user)                
                    if hostfeedback:
                        for h in hostfeedback:
                            print h.pk
                            if h.point is not None:
                                total_sum=int(total_sum+h.point)
                            print "sum : ",total_sum
                            host_ranking=HostRanking.objects.filter(user=h.user_challenge_category_location_rel_rel.user)
                            if not host_ranking:
                                rank=HostRanking.objects.create(user=h.user_challenge_category_location_rel_rel.user,host_point=total_sum)
                            else:
                                host_ranking.update(host_point=total_sum)
                    
        return HostRanking.objects.all().order_by('-host_point')


class GetGifterRanking(generics.ListAPIView):
    serializer_class= GifterRankingSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.kwargs['user_id']
        print "user : ",user
             
        host_user= AuthUserGroups.objects.filter(user=User.objects.get(pk=user),group=Group.objects.get(pk=2))
        if host_user:
            gifter_challenge_queryset=MyChallengeRelRel.objects.filter(status=StatusType.objects.get(status='complete'))
            if gifter_challenge_queryset:
                for challenge in gifter_challenge_queryset:
                    total_sum=0
                    gifterfeedback=GifterFeedback.objects.filter(gift_user=challenge.user)                
                    if gifterfeedback:
                        for g in gifterfeedback:
                            print g.pk
                            if g.point is not None:
                                total_sum=int(total_sum+g.point)
                            print "sum : ",total_sum
                            gifter_ranking=GifterRanking.objects.filter(gift_user=g.gift_user)
                            if not gifter_ranking:
                                rank=GifterRanking.objects.create(gift_user=g.gift_user,gifter_point=total_sum)
                            else:
                                gifter_ranking.update(gifter_point=total_sum)
                    
        return GifterRanking.objects.all().order_by('-gifter_point')
    
        
class GetNotificationInboxForHost(generics.ListAPIView):
    serializer_class= NotificationSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.kwargs['user_id']
        print user
        auth_user=AuthUserGroups.objects.get(user=User.objects.get(pk=user),group=Group.objects.get(pk=1))
        return NotificationInbox.objects.filter(user=auth_user).order_by('-msg_generated_date')          
    

class GetNotificationInboxForGifter(generics.ListAPIView):
    serializer_class= NotificationSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.kwargs['user_id']
        print user 
        auth_user=AuthUserGroups.objects.get(user=User.objects.get(pk=user),group=Group.objects.get(pk=2))
        return NotificationInbox.objects.filter(user=auth_user).order_by('-msg_generated_date')

class GetHostRating(generics.ListAPIView):
    serializer_class= HostRatingSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.kwargs['user_id']
        print user 
        host_user= AuthUserGroups.objects.filter(user=User.objects.get(pk=user),group=Group.objects.get(pk=1))
        if host_user:
            userchallenge=HostRating.objects.filter(user=host_user[0].pk)
            return userchallenge
        else:
            raise APIException("Invalid User")
        
class GetGifterRating(generics.ListAPIView):
    serializer_class= GifterRatingSerializer
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user=self.kwargs['user_id']
        print user
        gift_user= AuthUserGroups.objects.filter(user=User.objects.get(pk=user),group=Group.objects.get(pk=2))
        if gift_user:
            gifterchallenge=GifterRating.objects.filter(gift_user=gift_user[0].pk)
            return gifterchallenge
        else:
            raise APIException("Invalid User") 



class CheckHostFeedback(generics.ListAPIView):
    queryset = HostFeedback.objects.all() 
    serializer_class= HostFeedbackSerializer
    authentication_classes = (TokenAuthentication,)	
    def get_queryset(self):
        hostfeedback=HostFeedback.objects.filter(user_challenge_category_location_rel_rel=self.kwargs['challenge_id'],gift_user=self.kwargs['user_id'])                
        if hostfeedback:
            return hostfeedback
        else:
            return hostfeedback

class CheckGifterFeedback(generics.ListAPIView):
    queryset = GifterFeedback.objects.all() 
    serializer_class= GifterFeedbackSerializer
    authentication_classes = (TokenAuthentication,)
    
    def get_queryset(self):
        gift_user=MyChallengeRelRel.objects.filter(pk=self.kwargs['gifter'])
   	if gift_user:
         	gifterfeedback=GifterFeedback.objects.filter(user_challenge_category_location=self.kwargs['challenge_id'],gift_user=gift_user[0].user)                
         	if gifterfeedback:
             		return gifterfeedback
         	else:
              		return gifterfeedback
