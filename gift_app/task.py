from celery.decorators import task
from celery.task import periodic_task
from datetime import datetime, timedelta
from models import UserChallengeCategoryLocationRelRel,MyChallengeRelRel,ChallengeType,StatusType,GiftergoalType
import datetime
from celery.schedules import crontab
from django.db.models import F
#from datetime import *#
from django.db.models import Q
from fcm_django.models import FCMDevice
from push_notifications.models import APNSDevice

 
@periodic_task(
    #run_every=(timedelta(seconds=59)),
    #run_every=crontab(minute='0', hour='1') ,          
    run_every=(crontab(minute=30, hour=0)),
    name="get_pastchallenge",
    ignore_result=False
) 

def get_pastchallenge():
     print("in task")
     challengetype=ChallengeType.objects.filter(start_date=datetime.datetime.now().date()+timedelta(days=3))
     userchallenge=UserChallengeCategoryLocationRelRel.objects.filter(challenge__in=challengetype,status=StatusType.objects.get(status='host_approve'))        
     mychallenge=MyChallengeRelRel.objects.filter(user_challenge_category_location__in=userchallenge,status=StatusType.objects.get(status='host_approve'))
     for myc in mychallenge:
        try: 
            print("user: ",FCMDevice.objects.filter(user=myc.user.user))
            mobile_device = FCMDevice.objects.filter(user=myc.user.user)
            #deviceiOS = APNSDevice.objects.filter(user=myc.user.user)
            print("devices to which notifications is sent: ",mobile_device)
            message="Dear "+ myc.user.user.email+", this is a reminder message to inform you that challenge "+ myc.user_challenge_category_location.challenge.title +" is about to start on "+myc.user_challenge_category_location.challenge.start_date +" , "+myc.user_challenge_category_location.challenge.start_time+" We look forward to your timely participation and make it a success."
            print message
            mobile_device.send_message("Challenge Reminder ",message)
            #deviceiOS.send_message(message)
            NotificationInbox.objects.create(message=message,user=myc.user,msg_generated_date=datetime.datetime.now())
            print("message sent")
        except Exception as e:
            print("exception------------------------------------------",e.message) 
    
     # 1 day before notification 
     challengetype=ChallengeType.objects.filter(start_date=datetime.datetime.now().date()+timedelta(days=1))
     userchallenge=UserChallengeCategoryLocationRelRel.objects.filter(challenge__in=challengetype,status=StatusType.objects.get(status='host_approve'))        
     mychallenge=MyChallengeRelRel.objects.filter(user_challenge_category_location__in=userchallenge,status=StatusType.objects.get(status='host_approve'))
     for myc in mychallenge:
        try: 
            print("user: ",FCMDevice.objects.filter(user=myc.user.user))
            mobile_device = FCMDevice.objects.filter(user=myc.user.user)
            #deviceiOS = APNSDevice.objects.filter(user=myc.user.user)
            print("devices to which notifications is sent: ",mobile_device)
            message="Dear "+ myc.user.user.email+", this is a reminder message to inform you that challenge "+ myc.user_challenge_category_location.challenge.title +" is about to start on "+myc.user_challenge_category_location.challenge.start_date +" , "+myc.user_challenge_category_location.challenge.start_time+" We look forward to your timely participation and make it a success."
            mobile_device.send_message("Challenge Reminder ",message)
            #deviceiOS.send_message(message)
            NotificationInbox.objects.create(message=message,user=myc.user,msg_generated_date=datetime.datetime.now())
            print("message sent")
        except Exception as e:
            print("exception------------------------------------------",e.message) 
     #changes status of gifer & host challenges when challenges end date expire
     challenge=ChallengeType.objects.filter(end_date=datetime.datetime.now().date()-timedelta(days=1))
     if challenge:
         #print challenge
         status=StatusType.objects.get(status='complete')
         #flag=0
         for c in challenge:
            
             #print "time : ",c.end_time,c.start_time
             d1 =c.start_date# date.datetime.strptime(c.start_date, "%Y-%m-%d")
             d2 = c.end_date#datetime.datetime.strptime(c.end_date, "%Y-%m-%d")
             days= int(abs((d2 - d1).days))
             print "days - ",days
             time1 = datetime.datetime.strptime(""+str(c.end_time),'%H:%M:%S')
             time2 = datetime.datetime.strptime(""+str(c.start_time),'%H:%M:%S')
             t3 = time1-time2
             print "time difference:",t3     
             #t3=datetime.combine(date.today(), c.end_time) - datetime.combine(date.today(), c.start_time)
              
             t4=t3.total_seconds()
             print "seconds : ",t4
             tot_mins=int(t4/60.0)
             final_min=0
             if int(days)>0:
                print("within if condition " ,tot_mins)
                final_min=tot_mins*int(days+1)
             else:
                final_min=tot_mins
             print "final_min :",final_min
             user_challenge=UserChallengeCategoryLocationRelRel.objects.filter(~Q(status = StatusType.objects.get(status='complete')),status = StatusType.objects.get(status='host_approve'),challenge=c)
             #print ("flag",flag)
             if user_challenge:
                for uc in user_challenge:
                    uc.status=status
                    uc.save()
                    my_user_challenge=MyChallengeRelRel.objects.filter(~Q(status = StatusType.objects.get(status='complete')),status = StatusType.objects.get(status='host_approve'),user_challenge_category_location=uc)
                   
                    if my_user_challenge:
                        for muc in my_user_challenge:
                            muc.status=status
                            muc.save()  
                            setgoal=GiftergoalType.objects.filter(user=muc.user)
                            if setgoal: 
                                print "completed task-----------",setgoal
                                 
                                for s in setgoal:
                                    print ("@@@@@@@@ : ", GiftergoalType.objects.filter(pk=s.pk))
                                    print("Before : ",s.completed_hours)
                                    #GiftergoalType.objects.filter(user=muc.user).update(completed_tasks=F("completed_tasks") + 1) 
                                    
                                    
                                    s.completed_tasks=s.completed_tasks+1
                                    if s.completed_hours==0:
                                        #print("flag ",flag)
                                        s.completed_hours=int(s.goal_hours-final_min)
                                    else:
                                        #print("within else ",flag)
                                        s.completed_hours=int(s.completed_hours-final_min)
                                        
                                    s.save()
                                   
                                    print("After : ",s.completed_hours)
               # flag=1                      
     print("in get past challenge task")  