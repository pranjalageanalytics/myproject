from __future__ import division
from django.contrib.auth.models import User,Group
 
from rest_framework import serializers, exceptions
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from json import loads, dumps
from django.db.models import F
import datetime
from .models import LocationType,CategoryType,ChallengeType,UserChallengeCategoryLocationRelRel,StatusType,\
UserCategoryRel,UserLocationRel,MyChallengeRelRel,StatusType,GiftergoalType,UserType,AuthUserGroups,UserChallengeCategoryLocationRelRelCategory,\
UserChallengeCategoryLocationRelRelLocation,HostFeedback,GifterFeedback,GifterRanking,HostRanking,HostRating,NotificationInbox,GifterRating,\
GifterRating,Reward
#from rest_auth.serializers import AuthGroupSerializer
from rest_auth.serializers import UserSerializer
from django.contrib.auth import get_user_model
UserModel = get_user_model()
import base64
import os
from django.core.files import File 
from fcm_django.models import FCMDevice
from push_notifications.models import APNSDevice
from notifications.signals import notify
from django.conf import settings
get_media=settings.MEDIA_ROOT


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationType
        fields = ('id','city', 'province', 'lattitude', 'longitude')
         
class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StatusType
        fields = ('id','status')
         
         
class CategoryTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoryType
        fields = ('category_id','category_name','category_image')
         
        
#^[0-9\-\+]{9,15}$----->works for 0771234567 and +0771234567
class PhoneNumberValidator(RegexValidator):
    regex = r'^[0-9\-\+]+$'
    message = 'Invalid Phone Number'
         
class ChallengeSerializer(serializers.ModelSerializer):
    contact_no = serializers.CharField(
        required=False,
        min_length=12,
        max_length=13,
        error_messages={
            "blank": "Contact number cannot be empty",
            "min_length": "phone number should be 12 digit long",
            "max_length": "phone number should be 12 digit long",
        },validators=[PhoneNumberValidator()]
    )
    requested_volunteers= serializers.RegexField(regex=r'^[0-9]+$', required=False, error_messages= {"invalid" : 'Please Enter No Only'})
     
    class Meta:
        model=ChallengeType
        fields=('title','start_date','end_date','reg_expire_date','start_time','end_time','description',
                'requested_volunteers','contact_no','venue','direction')
     
    def validate(self, data):
        if data['start_date']:
            print "start date : ",data['start_date']
            if data['start_date'] <= datetime.datetime.now().date():
                print "within start validation"
                raise serializers.ValidationError("Registration start date should be greater than today's date")
        if data['end_date']:
            print "end date : ",data['end_date']
            if data['end_date'] < data['start_date']:
                print "within start & end date validation"
                raise serializers.ValidationError("Registration start date cannot be less than Registration End date")
        if data['reg_expire_date']:
            if data['reg_expire_date'] > data['end_date']:
                raise serializers.ValidationError("Registration expiry date cannot be more than Registration End date") 
        return data
 
class UserCategoryCreateSerializer(serializers.ModelSerializer):
    #category=serializers.MultipleChoiceField(choices=CategoryType.objects.all())
    category = serializers.CharField(source='category.category_name')
    class Meta:
        model=UserCategoryRel
        fields=('pk','category',)     
    
     
class UserCategoryUpdateSerializer(serializers.ModelSerializer):
    category=serializers.MultipleChoiceField(choices=CategoryType.objects.all())
    class Meta:
        model=UserCategoryRel
        fields=('category',) 
    def update(self, instance, validated_data):
        request = self.context.get("request")
        user= request.user    
        print user.pk  
        categories = validated_data.pop('category')
        queryset=UserCategoryRel.objects.filter(user=user.pk)
        #for instance in queryset:
             
        for category in categories:
            instance.category = validated_data.get('category', category)
            instance.user = validated_data.get('user', instance.user)
            instance.save()
        return instance
     
 
class UserLocationCreateSerializer(serializers.ModelSerializer):
    location=serializers.CharField(source='location.city')
    user=serializers.CharField(source='user.user')
    class Meta:
        model=UserLocationRel
        fields=('location','user')     
 
     
class GetGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model=GiftergoalType
        #fields=('pk','goal_start_date','goal_end_date','goal_hours','goal_tasks','completed_hours','completed_tasks')
        fields=('pk','goal_hours','goal_tasks','completed_hours','completed_tasks')
 
class GetGoalPercentageSerializer(serializers.ModelSerializer):
    completed_hours=serializers.IntegerField()
    completed_tasks=serializers.IntegerField()
    class Meta:
        model=GiftergoalType
        fields=('pk','goal_hours','goal_tasks','completed_hours','completed_tasks')

class GoalSerializer(serializers.ModelSerializer):
    completed_hours=serializers.DecimalField(max_digits=4, decimal_places=2)
    completed_tasks=serializers.DecimalField(max_digits=4, decimal_places=2)
    class Meta:
        model = GiftergoalType
        #fields=('goal_start_date','goal_end_date','goal_hours','goal_tasks','completed_hours','completed_tasks')
        fields=('goal_hours','goal_tasks','completed_hours','completed_tasks')
         
class UpdateGoalSerializer(serializers.ModelSerializer): 
    class Meta:
        model=GiftergoalType
        # fields=('goal_start_date','goal_end_date','goal_hours','goal_tasks')    
        fields=('goal_hours','goal_tasks')
    
    def update(self, instance, validated_data):      
        #instance.goal_start_date = validated_data.get('goal_start_date', instance.goal_start_date)
        #instance.goal_end_date = validated_data.get('goal_end_date', instance.goal_end_date)
        goal_hours= validated_data.get('goal_hours', instance.goal_hours)
        #goal_tasks= validated_data.get('goal_tasks', instance.goal_tasks)  
        goal_minutes=int(goal_hours)*60
        instance.goal_hours = goal_minutes
        instance.goal_tasks = validated_data.get('goal_tasks', instance.goal_tasks)        
        instance.save()
        return instance
     
     
class SetGoalSerializer(serializers.ModelSerializer):
    goal_hours=serializers.FloatField(required=False)
    goal_tasks=serializers.IntegerField(required=False)
    class Meta:
        model=GiftergoalType
        fields=('goal_hours','goal_tasks')
        #fields=('goal_start_date','goal_end_date','goal_hours','goal_tasks')
 
    def create(self,validated_data):
        request = self.context.get("request")
        user= request    
        
        gifter_user= AuthUserGroups.objects.filter(user=User.objects.get(pk=user),group=Group.objects.get(pk=2))
        if gifter_user:
            gifter_goal=GiftergoalType.objects.filter(user=gifter_user[0])
            if not gifter_goal: 
                hours=0
                print "gifter_user",gifter_user
                validated_data['user']=gifter_user[0]
                print "validated_data['goal_hours'] : ",validated_data.get('goal_hours')
                if validated_data.get('goal_hours')==None:
                    validated_data['goal_hours']=0
                else:
                    hours=validated_data.get('goal_hours')
                    tot_mins=int(hours*60)
                    validated_data['goal_hours']=tot_mins
                if validated_data.get('goal_tasks')==None: 
                    validated_data['goal_tasks']=0                    
               
                validated_data['completed_tasks']=0
                validated_data['completed_hours']=0
                print validated_data['goal_hours']
                
                GiftergoalTypeObj=GiftergoalType.objects.create(**validated_data)
                return GiftergoalTypeObj
            else:
                print "within else"
                msg = _('You have already set goals for same user')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Invalid User')
            raise exceptions.ValidationError(msg)
        
         
         
    """def validate(self, data):
        if data['goal_end_date']:
            print "goal end date : ",data['goal_end_date']
            if data['goal_end_date'] < data['goal_start_date']:
                print "within start & end date validation"
                raise serializers.ValidationError("Goal start date cannot be less than Goal End date")    
        return data"""
     
class UserListSerializer(UserSerializer):
    organization = serializers.CharField(source="usertype.organization")
 
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('organization',)
      
class AuthGroupSerializer(serializers.ModelSerializer):
    user= UserListSerializer()
    class Meta:
        model = AuthUserGroups
        fields = ('user',)
 
class ChallengeListSerializer (serializers.ModelSerializer):
    class Meta:
        model=ChallengeType
        fields=('title','start_date','end_date','reg_expire_date','start_time','end_time','description',
                'requested_volunteers','contact_no','venue','direction','accepted_volenteers_by_host','declined_volenteers_by_host',
                'commited_volunteers','decline_volunteers','tentative_volunteers')
         
class HostRatingSerializer(serializers.ModelSerializer): 
    class Meta:
        model=HostRating
        fields=('host_rating', )
        
class GifterRatingSerializer(serializers.ModelSerializer): 
    class Meta:
        model=GifterRating
        fields=('gifter_rating', ) 
             
class UserChallengeCategoryLocationListSerializer(serializers.ModelSerializer):
    user=AuthGroupSerializer()
    categorytype = serializers.StringRelatedField(many=True)
    locationtype = serializers.StringRelatedField(many=True)
    challenge=ChallengeListSerializer()
    status=serializers.CharField(source="status.status")
    host_rating=HostRatingSerializer()
    class Meta :
        model=UserChallengeCategoryLocationRelRel
        fields=('pk','user','categorytype','locationtype','challenge','status','photo','host_rating')
            
class UserChallengeCategoryLocationRelRelSerializer(serializers.HyperlinkedModelSerializer):    
    #category_location=CategoryLocationM2MSerializer()
    categorytype = serializers.PrimaryKeyRelatedField(queryset=CategoryType.objects.all(),many=True)
    locationtype = serializers.PrimaryKeyRelatedField(queryset=LocationType.objects.all(),many=True) 
    challenge=ChallengeSerializer()
    photo=serializers.ImageField(source=get_media,required=False)
    class Meta:
        model=UserChallengeCategoryLocationRelRel
        fields=('pk','categorytype','locationtype','challenge','photo')
         
    def create(self,validated_data):
        request = self.context["request"]
        group_id = self.context["group_id"]   
        #print self.request.user
        if group_id=='1':
            user= request   
            print user
            usertype= UserType.objects.filter(user= user)
            if usertype[0].host_permission=='3': 
                authuser=AuthUserGroups.objects.filter(user=usertype[0].user,group=Group.objects.get(pk=1))
                if authuser:
                        categories=validated_data.pop('categorytype')
                        print("category : ", categories)
                        locations=validated_data.pop('locationtype')
                        print("location : ", locations)
                        challenge_data=validated_data.pop('challenge')
                        challenge_data['post_date']=datetime.datetime.now()
                        challenge_data['commited_volunteers']=0
                        challenge_data['decline_volunteers']=0
                        challenge_data['tentative_volunteers']=0
                        challenge_data['accepted_volenteers_by_host']=0
                        challenge_data['declined_volenteers_by_host']=0
                        print "description : ",challenge_data['description']
                        if challenge_data['description']=='':
                            challenge_data['description']='No description provided by host'
                        if challenge_data['direction']=='':
                            challenge_data['direction']='No direction provided by host'
                        challenge=ChallengeType.objects.create(**challenge_data)
                        validated_data['challenge']=challenge
                        validated_data['user']=authuser[0]
                        validated_data['status']=StatusType.objects.get(status='pending')
                        validated_data['host_rating']=HostRating.objects.get(user=authuser[0])
                        UserChallengeCategoryLocationRel=UserChallengeCategoryLocationRelRel.objects.create(**validated_data)
                        if categories:
                            for category in categories:
                                obj1=UserChallengeCategoryLocationRelRelCategory.objects.create(userchallengecategorylocationrelrel=UserChallengeCategoryLocationRel,categorytype=category )
                                       
                        if locations:
                            for location in locations:
                                obj2=UserChallengeCategoryLocationRelRelLocation.objects.create(userchallengecategorylocationrelrel=UserChallengeCategoryLocationRel,locationtype=location)
                            #print obj
                        
                        
                        
                        obj=User.objects.all()
                        admin_user=User.objects.filter(email='admin@gmail.com')
                        msg='New Challenge appeared from Host '+authuser[0].user.email+' for Approval'
                        notify.send(authuser[0].user, recipient=admin_user[0], verb=msg)
                        """rating=1.0
                        total_sum=0
                        hostfeedback=HostFeedback.objects.filter(host_user=authuser[0])
                        if hostfeedback:
                            cnt=hostfeedback.count()
                            total_count=int(cnt*5)
                            print "total_count : ",total_count
                            for h in hostfeedback:
                                total_sum=int(total_sum+h.point)
                            print "total_sum : ",total_sum
                            div=float(total_sum/total_count)
                            print div
                            rating=(total_sum/total_count)*5
                        host_rating=UserChallengeCategoryLocationRelRel.objects.filter(user=authuser[0])
                        #for h in host_rating:
                        host_rating.update(host_rating=rating)"""
                        return UserChallengeCategoryLocationRel
                        #return None
                else:
                        msg = _('Invalid User')
                        raise exceptions.ValidationError(msg)
            elif usertype[0].host_permission=='2':
                msg = _('Host Rejected')
                raise exceptions.ValidationError(msg)
            else:
                msg = _('Permission Denied')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Invalid User')
            raise exceptions.ValidationError(msg)
        
class ChallengeImageSerializer(serializers.ModelSerializer):
     
    class Meta:
            model=ChallengeType
            fields=('photo',)
             
class UpdateChallengeImageSerializer(serializers.ModelSerializer):
    #challenge=ChallengeImageSerializer()
    class Meta:
            model=UserChallengeCategoryLocationRelRel
            fields=('photo',)
         
    def update(self, instance, validated_data):
            print("hiii  ",validated_data.get('photo'))
            #userchallenge=UserChallengeCategoryLocationRelRel.objects.get(pk=instance.pk)
            instance.photo=validated_data.get('photo', instance.photo) #challenge_data.get('photo',challenge.photo)
            instance.save()
            return instance
 
             
 
   
class UserChallengeCategoryLocation_RetriveUpdateSerializer(serializers.ModelSerializer):
    categorytype = serializers.PrimaryKeyRelatedField(queryset=CategoryType.objects.all(),many=True)
    locationtype = serializers.PrimaryKeyRelatedField(queryset=LocationType.objects.all(),many=True) 
    challenge=ChallengeSerializer()
     
    class Meta:
        model=UserChallengeCategoryLocationRelRel
        fields=('pk','categorytype','locationtype','challenge','photo')
         
    def update(self,instance,validated_data):
        #print self.context.get("request").user
        group_id=self.context["group_id"] 
        if group_id=='1': 
            usercategory=UserChallengeCategoryLocationRelRelCategory.objects.filter(userchallengecategorylocationrelrel=instance)
            for category in usercategory:
                category.delete()
            userlocation=UserChallengeCategoryLocationRelRelLocation.objects.filter(userchallengecategorylocationrelrel=instance)
            for location in userlocation:
                location.delete()
            categories=validated_data.pop('categorytype')
            print("category : ", categories)
            locations=validated_data.pop('locationtype')
            print("location : ", locations)         
            challenge_data=validated_data.pop('challenge')
            challenge=instance.challenge
            challenge.title=challenge_data.get('title',challenge.title)
            #challenge.photo=challenge_data.get('photo',challenge.photo)
            challenge.start_date=challenge_data.get('start_date',challenge.start_date)
            challenge.end_date=challenge_data.get('end_date',challenge.end_date)
            challenge.start_time=challenge_data.get('start_time',challenge.start_time)
            challenge.end_time=challenge_data.get('end_time',challenge.end_time)
            challenge.venue=challenge_data.get('venue',challenge.venue)
            challenge.contact_no=challenge_data.get('contact_no',challenge.contact_no)
            challenge.description=challenge_data.get('description',challenge.description)
            challenge.reg_expire_date=challenge_data.get('reg_expire_date',challenge.reg_expire_date)
            challenge.direction=challenge_data.get('direction',challenge.direction)
            #instance.status=StatusType.objects.get(status='pending')
            instance.save()
            challenge.requested_volunteers=challenge_data.get('requested_volunteers',challenge.requested_volunteers)
            if categories:
                for category in categories:
                    obj1=UserChallengeCategoryLocationRelRelCategory.objects.create(userchallengecategorylocationrelrel=instance,categorytype=category )
                                       
            if locations:
                for location in locations:
                    obj2=UserChallengeCategoryLocationRelRelLocation.objects.create(userchallengecategorylocationrelrel=instance,locationtype=location)
                         
            challenge.save()
            my_challenge=MyChallengeRelRel.objects.filter(user_challenge_category_location=instance,status=StatusType.objects.get(pk=7)) 
            for myc in my_challenge:
                try: 
                    #print("user: ",FCMDevice.objects.filter(user=gifter.user.user))
                    device = FCMDevice.objects.filter(user=myc.user.user)
                    deviceiOS = APNSDevice.objects.filter(user=myc.user.user)
                    #print("devices to which notifications is sent: ",device)
                    message="Dear Gifter "+str(myc.user.user.email)+", your challenge "+ str(challenge) +" has been updated.  Kindly check challenge details. "
                    device.send_message("Challenge Update",message)
                    deviceiOS.send_message(message)
                    NotificationInbox.objects.create(message=message,user=myc.user,msg_generated_date=datetime.datetime.now())
                    print("message sent")
                except Exception as e:
                    print("exception------------------------------------------1",e.message)
            return instance
        else:
            msg = _('Invalid User')
            raise exceptions.ValidationError(msg)
    
class CreateMyChallengeSerializer(serializers.ModelSerializer):
    FAVOURITE_CHOICES = (
        ('1', 'Yes'),
        ('2', 'No'),
    )
 
    #is_favourite = serializers.ChoiceField(choices=FAVOURITE_CHOICES,null=True)
    class Meta:
        model=MyChallengeRelRel
        #fields=('user_challenge_category_location','is_favourite','status')  
        fields=('user_challenge_category_location','status')
         
    def create(self,validated_data):
        request = self.context["request"]
        group_id = self.context["group_id"]   
        #print "group_id :" ,group_id
        if group_id=='2':
            
            authuser=[]
            usertype= User.objects.filter(pk= request)
            print "usertype ",usertype
            if usertype:
                authuser=AuthUserGroups.objects.filter(user=usertype[0],group=Group.objects.get(pk=2))
            else:
                msg = _('Invalid User')
                raise exceptions.ValidationError(msg)
            if authuser:            
                print "gift_user",authuser[0].user
                print "challenge:",self.context["challenge_id"]
                # print validated_data.get('status')
                var=validated_data.get('status')
                print var.id
                if var.id==2 or var.id==4 or var.id==5: 
                #track_data=validated_data.pop('category_location')
                    challenge=UserChallengeCategoryLocationRelRel.objects.filter(pk=self.context["challenge_id"])
                    
                    mychallenge= MyChallengeRelRel.objects.filter(user_challenge_category_location=challenge[0],user=authuser)
                    if not mychallenge:
                        validated_data['user']=authuser[0]                     
                        validated_data['user_challenge_category_location']=challenge[0]
                        validated_data['challenge_join_date']=datetime.datetime.now()
                        validated_data['is_favourite']='2'
                        validated_data['gifter_rating']=GifterRating.objects.get(gift_user=authuser[0])
                        mychallenge_rel=MyChallengeRelRel.objects.create(**validated_data)
                        """rating=1.0
                        total_sum=0
                        gifterfeedback=GifterFeedback.objects.filter(gift_user=authuser[0])
                        if gifterfeedback:
                            cnt=gifterfeedback.count()
                            total_count=int(cnt*5)
                            print "total_count : ",total_count
                            for h in gifterfeedback:
                                total_sum=int(total_sum+h.point)
                            print "total_sum : ",total_sum
                            div=float(total_sum/total_count)
                            print div
                            rating=(total_sum/total_count)*5
                        gifter_rating=MyChallengeRelRel.objects.filter(user=authuser[0])
                        #for h in host_rating:
                        gifter_rating.update(gifter_rating=rating)"""
                        
                        c=ChallengeType.objects.filter(pk=challenge[0].challenge.pk)
                        if challenge:
                            if var.id==2: 
                                print "within approve"             
                                c.update(commited_volunteers=F("commited_volunteers") + 1)  
                                try: 
                                    print("user: ",FCMDevice.objects.filter(user=challenge[0].user.user))
                                    mobile_device = FCMDevice.objects.filter(user=challenge[0].user.user)
                                    deviceiOS = APNSDevice.objects.filter(user=challenge[0].user.user)
                                    print("devices to which notifications is sent: ",mobile_device)
                                    message="Dear Host "+ challenge[0].user.user.email+", Gifter "+ authuser[0].user.email+" is interested to join the challenge "+challenge[0].challenge.title
                                    mobile_device.send_message("Gifter Join Challenge ",message)
                                    deviceiOS.send_message(message)
                                    NotificationInbox.objects.create(message=message,user=challenge[0].user,msg_generated_date=datetime.datetime.now())
                                    print("message sent")
                                except Exception as e:
                                    print("exception------------------------------------------",e.message) 
                                             
                            elif var.id==4:
                                c.update(decline_volunteers=F("decline_volunteers") + 1)                
                            elif var.id==5:
                                c.update(tentative_volunteers=F("tentative_volunteers") + 1)     
                             
                            return mychallenge_rel
                    else:
                        myc =MyChallengeRelRel.objects.get(pk=mychallenge[0].pk)
                        print myc.status.pk
                        status=  validated_data.get('status')   
                        #is_favourite=  validated_data.get('is_favourite', instance.is_favourite)
                        mychallenge[0].status = status 
                        #instance.is_favourite=is_favourite  
                        mychallenge[0].save()        
                        userchallenge=UserChallengeCategoryLocationRelRel.objects.get(pk=myc.user_challenge_category_location.pk)
                        c=ChallengeType.objects.filter(pk=userchallenge.challenge.pk)
                        print c
                        if myc.status.pk==2:    
                            c.update(commited_volunteers=F("commited_volunteers") - 1) 
                        elif myc.status.pk==4: 
                            c.update(decline_volunteers=F("decline_volunteers") - 1)  
                        elif myc.status.pk==5: 
                            c.update(tentative_volunteers=F("tentative_volunteers") - 1) 
                        elif myc.status.pk==7: 
                            print "new condition"
                            c.update(accepted_volenteers_by_host=F("accepted_volenteers_by_host") - 1)
                            if status.pk==4: 
                                c.update(decline_volunteers=F("decline_volunteers") + 1)
                                c.update(commited_volunteers=F("commited_volunteers") - 1) 
                                pass
                            elif status.pk==5: 
                                c.update(tentative_volunteers=F("tentative_volunteers") + 1) 
                                c.update(commited_volunteers=F("commited_volunteers") - 1) 
                                pass
                        if status.pk==2:
                            try: 
                                    print("user: ",FCMDevice.objects.filter(user=userchallenge.user.user))
                                    mobile_device = FCMDevice.objects.filter(user=userchallenge.user.user)
                                    deviceiOS = APNSDevice.objects.filter(user=userchallenge.user.user)
                                    print("devices to which notifications is sent: ",mobile_device)
                                    message="Dear Host "+ userchallenge.user.user.email+", Gifter "+ myc.user.user.email+" is interested to join the challenge "+userchallenge.challenge.title
                                    print message 
                                    mobile_device.send_message("Gifter Join Challenge ",message)
                                    deviceiOS.send_message(message)
                                    NotificationInbox.objects.create(message=message,user=userchallenge.user,msg_generated_date=datetime.datetime.now())
                                    print("message sent")
                            except Exception as e:
                                    print("exception------------------------------------------",e.message)     
                            c.update(commited_volunteers=F("commited_volunteers") + 1) 
                        elif status.pk==4 and myc.status.pk!=7: 
                            c.update(decline_volunteers=F("decline_volunteers") + 1)  
                        elif status.pk==5 and myc.status.pk!=7: 
                            c.update(tentative_volunteers=F("tentative_volunteers") + 1) 
                        
                    
                        return mychallenge[0]     
                                         
                else:
                    msg = _('Invalid Status')
                    raise exceptions.ValidationError(msg)
            else:
                msg = _('Invalid User')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Invalid User')
            raise exceptions.ValidationError(msg)
 
 
 
class MyChallengeListSerializer(serializers.ModelSerializer):
    challenge=serializers.CharField(source='user_challenge_category_location.challenge.title')
    user=serializers.CharField(source='user.user')
    status=serializers.CharField(source='status.status')
    gifter_rating=GifterRatingSerializer()
    class Meta:
        model=MyChallengeRelRel
        fields=('pk','user','challenge','status','gifter_rating') 
 
class UserMyChallengeSerializer(serializers.ModelSerializer):
    user=AuthGroupSerializer()
    categorytype = serializers.StringRelatedField(many=True)
    locationtype = serializers.StringRelatedField(many=True)
    challenge=ChallengeListSerializer()
    status=serializers.CharField(source="status.status")
    host_rating=HostRatingSerializer()
    class Meta :
        model=UserChallengeCategoryLocationRelRel
        fields=('pk','user','categorytype','locationtype','challenge','status','photo','host_rating')        
 
class GifterMyChallengeSerializer(serializers.ModelSerializer): 
    user_challenge_category_location=UserMyChallengeSerializer()
    #user=serializers.CharField(source='user.user')
    status=serializers.CharField(source='status.status')
    gifter_rating=GifterRatingSerializer()
    class Meta:
        model=MyChallengeRelRel
        fields=('user_challenge_category_location','status','challenge_join_date','is_favourite','gifter_rating')
 
         
class GifterAcceptanceSerializer(serializers.ModelSerializer):
    challenge=serializers.CharField(source='user_challenge_category_location.challenge.title')
    user=serializers.CharField(source='user.user')
     
    class Meta:
        model=MyChallengeRelRel
        fields=('user','challenge','status')
         
    def update(self, instance, validated_data):
        request = self.context["request"]        
        gifter = MyChallengeRelRel.objects.get(pk=self.context["gifter"])
        status=  validated_data.get('status', instance.status)     
        instance.status =   status   
        instance.save()
        status=StatusType.objects.get(status=instance.status)
        print status
        userchallenge=UserChallengeCategoryLocationRelRel.objects.get(pk=instance.user_challenge_category_location.pk)
        c=ChallengeType.objects.filter(pk=userchallenge.challenge.pk)
        print c[0].title
        if status.pk==3:    
            print "within if : ",status.pk            
            c.update(declined_volenteers_by_host=F("declined_volenteers_by_host") + 1)
            c.update(commited_volunteers=F("commited_volunteers") - 1) 
            try: 
                print("user: ",FCMDevice.objects.filter(user=gifter.user.user))
                device = FCMDevice.objects.filter(user=gifter.user.user)
                deviceiOS = APNSDevice.objects.filter(user=gifter.user.user)
                print ("deviceiOS ",deviceiOS)
                print("devices to which notifications is sent: ",deviceiOS)
                message="Dear Gifter "+str(gifter.user.user.email)+",  We regret to inform you that your request for joining the challenge "+ str(c[0].title) +" has been declined.  Kindly contact us on "+ str(userchallenge.user.user.email)  +" for futher details"
                device.send_message("Gifter Decline",message)
                deviceiOS.send_message(message)
                NotificationInbox.objects.create(message=message,user=gifter.user,msg_generated_date=datetime.datetime.now())
                print("message sent")
            except Exception as e:
                print("exception------------------------------------------1",e.message) 
        elif status.pk==7: 
            print "in else"
            c.update(accepted_volenteers_by_host=F("accepted_volenteers_by_host") + 1)  
            
            try: 
                print("user: ",FCMDevice.objects.filter(user=gifter.user.user))
                device = FCMDevice.objects.filter(user=gifter.user.user)
                deviceiOS = APNSDevice.objects.filter(user=gifter.user.user)
                print("devices to which notifications is sent: ",deviceiOS)
                message="Dear Gifter "+ str(gifter.user.user.email) +", Congrats!!  We welcome you to paricipate in the Challenge "+str(c[0].title) +" and make it a success"
                device.send_message("Gifter Approval",message)
                deviceiOS.send_message(message)
                NotificationInbox.objects.create(message=message,user=gifter.user,msg_generated_date=datetime.datetime.now())
                print("message sent")
            except Exception as e:
                print("exception------------------------------------------2",e) 
        return instance
         
class UpdateMyChallengeSerializer(serializers.ModelSerializer):
    FAVOURITE_CHOICES = (
        ('1', 'Yes'),
        ('2', 'No'),
    )
 
    is_favourite = serializers.ChoiceField(choices=FAVOURITE_CHOICES,required=False)
    class Meta:
        model=MyChallengeRelRel
        fields=('user_challenge_category_location','is_favourite','status') 
         
    def update(self, instance, validated_data):
        #status=StatusType.objects.get(status=instance.status)
        #print status
        myc =MyChallengeRelRel.objects.get(pk=instance.pk)
        print myc.status.pk
        status=  validated_data.get('status', instance.status)   
        is_favourite=  validated_data.get('is_favourite', instance.is_favourite)
        instance.status = status 
        #instance.is_favourite=is_favourite  
        instance.save()        
        userchallenge=UserChallengeCategoryLocationRelRel.objects.get(pk=instance.user_challenge_category_location.pk)
        c=ChallengeType.objects.filter(pk=userchallenge.challenge.pk)
        print c
        if myc.status.pk==2:    
            c.update(commited_volunteers=F("commited_volunteers") - 1) 
        elif myc.status.pk==4: 
            c.update(decline_volunteers=F("decline_volunteers") - 1)  
        elif myc.status.pk==5: 
            c.update(tentative_volunteers=F("tentative_volunteers") - 1) 
        elif myc.status.pk==7: 
            print "new condition"
            c.update(accepted_volenteers_by_host=F("accepted_volenteers_by_host") - 1)
            if status.pk==4: 
                c.update(decline_volunteers=F("decline_volunteers") + 1)
                c.update(commited_volunteers=F("commited_volunteers") - 1) 
                pass
            elif status.pk==5: 
                c.update(tentative_volunteers=F("tentative_volunteers") + 1) 
                c.update(commited_volunteers=F("commited_volunteers") - 1) 
                pass
        if status.pk==2:    
            c.update(commited_volunteers=F("commited_volunteers") + 1) 
        elif status.pk==4 and myc.status.pk!=7: 
            c.update(decline_volunteers=F("decline_volunteers") + 1)  
        elif status.pk==5 and myc.status.pk!=7: 
            c.update(tentative_volunteers=F("tentative_volunteers") + 1) 
        
        if status.pk!=2 and status.pk!=4 and status.pk!=5:
            msg = _('Invalid Status')
            raise exceptions.ValidationError(msg) 
        return instance 
          
class MakeMyFavouriteMyChallengeSerializer(serializers.ModelSerializer):
    FAVOURITE_CHOICES = (
        ('1', 'Yes'),
        ('2', 'No'),
    )
 
    is_favourite = serializers.ChoiceField(choices=FAVOURITE_CHOICES,required=False)
    class Meta:
        model=MyChallengeRelRel
        fields=('is_favourite',) 
         
    def create(self, validated_data):
        request = self.context["request"]
        group_id = self.context["group_id"]   
        print "MakeMyFavouriteMyChallengeSerializer :  ",self.context["challenge_id"]
        if group_id=='2':
            user= request   
            print user
            authuser=[]
            usertype= UserType.objects.filter(user= request)
            if usertype:
                authuser=AuthUserGroups.objects.filter(user=usertype[0].user,group=Group.objects.get(pk=2))
            else:
                msg = _('Invalid User')
                raise exceptions.ValidationError(msg)
            if authuser:            
                print "gift_user",authuser[0].user
                print "challenge:",self.context["challenge_id"]
                challenge=UserChallengeCategoryLocationRelRel.objects.filter(pk=self.context["challenge_id"])                    
                mychallenge= MyChallengeRelRel.objects.filter(user_challenge_category_location=challenge[0],user=authuser)
                if not mychallenge:
                        validated_data['user']=authuser[0]                     
                        validated_data['user_challenge_category_location']=challenge[0]
                        validated_data['challenge_join_date']=datetime.datetime.now()
                        validated_data['is_favourite']=validated_data.get('is_favourite')
                        validated_data['status']=StatusType.objects.get(status='pending')
                        validated_data['gifter_rating']=GifterRating.objects.get(gift_user=authuser[0])
                        mychallenge_rel=MyChallengeRelRel.objects.create(**validated_data)
                        return mychallenge_rel
                else:
                        mychallenge[0].is_favourite = validated_data.get('is_favourite')
                        mychallenge[0].save()
                        return mychallenge[0]
        else:
            msg = _('Invalid User')
            raise exceptions.ValidationError(msg)
    
     
class MyChallengeSerializer(serializers.ModelSerializer):
    challenge=serializers.CharField(source='user_challenge_category_location.challenge.title')
    user=serializers.CharField(source='user.user')
    class Meta:
        model=MyChallengeRelRel
        fields=('user','challenge')  
            
class UserCategorySerializer(serializers.ModelSerializer):
    #user=serializers.CharField(source='user', read_only=True)
    #category=serializers.CharField(source='category', read_only=True)
    class Meta:
        model=UserCategoryRel
        fields=('user','category')
        
class HostFeedbackSerializer(serializers.ModelSerializer):
    def create(self, validated_data):                 
        request=self.context["request"]
        challenge=UserChallengeCategoryLocationRelRel.objects.filter(pk=self.context["challenge_id"])
        authuser=AuthUserGroups.objects.filter(user=User.objects.get(pk=request),group=Group.objects.get(pk=2))
        user=User.objects.filter(pk=request)
        if authuser:
            mychallenge= MyChallengeRelRel.objects.filter(user_challenge_category_location=challenge[0],user=authuser[0],status=StatusType.objects.get(status='complete'))
            if mychallenge:               
                validated_data['gift_user']=user[0]                     
                validated_data['user_challenge_category_location_rel_rel']=challenge[0]
                validated_data['point']=validated_data.get('point') 
                validated_data['host_user']=challenge[0].user
                feedback=HostFeedback.objects.filter(user_challenge_category_location_rel_rel=challenge[0],gift_user=user[0])     
                if not feedback:
                    host_feedback=HostFeedback.objects.create(**validated_data)
                    total_sum=0
                    hostfeedback1=HostFeedback.objects.filter(host_user=challenge[0].user)
                    if hostfeedback1:
                            cnt=hostfeedback1.count()
                            total_count=int(cnt*5)
                            print "total_count : ",total_count
                            for h in hostfeedback1:
                                total_sum=int(total_sum+h.point)
                            print "total_sum : ",total_sum
                            div=float(total_sum/total_count)
                            print div
                            rating=(total_sum/total_count)*5
                    host_rating=HostRating.objects.filter(user=challenge[0].user)
                    host_rating.update(host_rating=rating)
                    return host_feedback
                else:
                    msg = _("Thank You! You have already submitted feedback for this challenge!")
                    raise exceptions.ValidationError(msg) 
                              
            else:
                msg = _("Challenge not completed,can't give feedback")
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Invalid User')
            raise exceptions.ValidationError(msg)
   
    class Meta:
        model=HostFeedback
        fields=('point',)
        
class GifterFeedbackSerializer(serializers.ModelSerializer):    
    def create(self, validated_data):
        gifter=self.context["gifter"]
        print gifter
        
        challenge=UserChallengeCategoryLocationRelRel.objects.filter(pk=self.context["challenge_id"])
        authuser=AuthUserGroups.objects.filter(pk=MyChallengeRelRel.objects.get(pk=gifter).user.pk,group=Group.objects.get(pk=2))
        if authuser:
            mychallenge= MyChallengeRelRel.objects.filter(user_challenge_category_location=challenge[0],user=authuser[0],status=StatusType.objects.get(status='complete'))
            if mychallenge:               
                validated_data['gift_user']=authuser[0]                     
                validated_data['user_challenge_category_location']=challenge[0]
                validated_data['point']=validated_data.get('point')
                mychallenge_user=MyChallengeRelRel.objects.get(pk=gifter)
                feedback=GifterFeedback.objects.filter(user_challenge_category_location=challenge[0],gift_user=mychallenge_user.user)     
                if not feedback:        
                    gifter_feedback=GifterFeedback.objects.create(**validated_data)
                    rating=1.0
                    total_sum=0
                    gifterfeedback=GifterFeedback.objects.filter(gift_user=mychallenge_user.user)
                    if gifterfeedback:
                            cnt=gifterfeedback.count()
                            total_count=int(cnt*5)
                            print "total_count : ",total_count
                            for h in gifterfeedback:
                                total_sum=int(total_sum+h.point)
                            print "total_sum : ",total_sum
                            div=float(total_sum/total_count)
                            print div
                            rating=(total_sum/total_count)*5
                    gifter_rating=GifterRating.objects.filter(gift_user=mychallenge_user.user)
                        #for h in host_rating:
                    gifter_rating.update(gifter_rating=rating)
                    return gifter_feedback
                else:
                    msg = _("Thank You! You have already submitted feedback for this challenge!")
                    raise exceptions.ValidationError(msg)
            else:
                msg = _("Gifter challenge not completed,can't give feedback")
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Invalid User')
            raise exceptions.ValidationError(msg)
    
    class Meta:
        model=GifterFeedback
        fields=('point',)
        
class GifterRankingSerializer(serializers.ModelSerializer):
    gift_user=serializers.CharField(source='gift_user.user')
    class Meta:
        model=GifterRanking
        fields=('gift_user','gifter_point')
        
class HostRankingSerializer(serializers.ModelSerializer):
    user=serializers.CharField(source='user.user')
    class Meta:
        model=HostRanking
        fields=('user','host_point')

        
class NotificationSerializer(serializers.ModelSerializer):
    #user=serializers.CharField(source='user.email')
    class Meta:
        model=NotificationInbox
        fields=('user','message','msg_generated_date')

class RewardSerializer(serializers.ModelSerializer):
    user=serializers.CharField(source='user.user')
    class Meta:
        model=Reward
        fields=('user','rewards_point',)   
        