from django.shortcuts import render,render_to_response,redirect
#from mygift import forms
#from gift_app import forms
from .forms import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import login as auth_login
from django.template import Context
from gift_app.models import *
from django.http import JsonResponse
from django.template import RequestContext
from .tables import *
from django.forms.models import model_to_dict
import logging   
from notifications.models import Notification
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
# from .utils import slug2id
from django.contrib.auth.decorators import login_required
from django.core.files import File 
from fcm_django.models import FCMDevice
from push_notifications.models import APNSDevice
import datetime
from django.contrib.auth.models import User,Group

logger = logging.getLogger('mygift')
logger.addHandler(logging.NullHandler())
# Create your views here.

def Login(request):
    logger.debug("In Login")
    form = loginForm()
        
    return render(request, "login.html", {'form':form})

def loginform(request):
 
 logger.debug("In Loginform")
 form = loginForm()
 try:
    if request.method == 'POST':
         
          username = request.POST.get('username')
          
          password = request.POST.get('password')
          
          user = authenticate(username =username, password=password)
          if user is not None:
            if user.is_active:
                print("login")
#                 logger.debug("User is active")
                request.session['user']=user.username
                auth_login(request, user)
                
                return redirect('/mygift/challenge/')
                return render(request,'base.html', {'user':user})
            else:
#                 logger.debug("User is not active")
                return render(request,'login.html', {'context1': "User is not active" , 'form':form})
          else:
#               logger.debug("Unknown User")
              return render(request,'login.html', {'context1': "Incorrect User Name or Password" , 'form':form})
    else:
          return render(request,'login.html')
 except Exception as e:
        print(e)
        return render(request,'login.html',{'context1':'User not found' , 'form':form}) 

@login_required(login_url="/mygift/login/")    
def host(request):
    logger.debug("In Host")
    UserTypeForm1 = UserTypeForm()
    context = RequestContext(request)
    authusergroup = AuthUserGroups.objects.filter(group = 1).order_by('-id')
    
    new_list=[]
    for obj in authusergroup:
        #print "user id is", obj.user.id
        userid = obj.user.id
        authuser = User.objects.get(id = userid)
        if authuser.is_active == 1:
         authuserid = authuser.id
        # print "authuserid..........",authuserid
         usergroup = UserType99.objects.get(user = userid)
        # print "id",usergroup.user.id
         new_list.append(usergroup )
        
       #  print "new list",new_list
        
        
         new_list.sort(key=lambda usergroup: usergroup.host_permission.lower())
#         
    HostList = UserTypeTable(new_list)
    
       
    return render(request,"host.html", {'HostList':HostList,'UserTypeForm':UserTypeForm1},context)
                        

@login_required(login_url="/mygift/login/")
def challenge(request):
  
    logger.debug("in challenge")
    
   
    usergroup = None
    context = RequestContext(request)
    ChallengeTypeForm1 = ChallengeTypeForm()
    CategoryLocationRelForm1 = CategoryLocationRelForm()
    UserTypeForm1 = UserTypeForm()
    AuthUserForm1=AuthUserForm()

    pending_queryset=UserChallengeCategoryLocationRelRel.objects.filter(status=StatusType.objects.get(status='pending')).order_by('-challenge__post_date')
    host_approve_queryset=UserChallengeCategoryLocationRelRel.objects.filter(status=StatusType.objects.get(status='host_approve')).order_by('-challenge__post_date')
    host_decline_queryset=UserChallengeCategoryLocationRelRel.objects.filter(status=StatusType.objects.get(status='host_decline')).order_by('-challenge__post_date')
    complete_challenge=UserChallengeCategoryLocationRelRel.objects.filter(status=StatusType.objects.get(status='complete')).order_by('-challenge__post_date')
    final_queryset=[]
    if pending_queryset:
        for k in pending_queryset:
          final_queryset.append(k)
    if host_approve_queryset:
        for k in host_approve_queryset:
          final_queryset.append(k)
    if host_decline_queryset:
        for k in host_decline_queryset:
          final_queryset.append(k)  
    
    if complete_challenge:
        for k in complete_challenge:
            final_queryset.append(k)
    
    #usergroup = UserChallengeCategoryLocationRelRel.objects.all().order_by('status','-id')
    #print usergroup
    
    ChallengeList = UserGroupsTable(final_queryset)
    print("list",final_queryset)
        
    return render(request,"challengeList.html", {'ChallengeList':ChallengeList,'ChallengeTypeForm':ChallengeTypeForm1 ,'CategoryLocationRelForm': CategoryLocationRelForm1 , 'UserTypeForm':UserTypeForm1,'AuthUserForm':AuthUserForm1},context)

        
       
def  hostapprove(request):
    logger.debug("In hostapprove")
    host = request.GET.get('host_id',None)
   
    AuthUserGroupsobj = AuthUserGroups.objects.get(id = host,group=Group.objects.get(pk=1))
    userid = AuthUserGroupsobj.user.id
    userobj = UserType.objects.get(user = userid)
   
    userobj.host_permission = "approve"
    userobj.save()


    
def challengeapprove(request):
    logger.debug("In challengeapprove")
    challenge = request.GET.get('challenge_id',None)
    
    usergroup = UserChallengeCategoryLocationRelRel.objects.get(id = challenge)
   
    challengeid = usergroup.challenge.challenge_id
    
    challengeobj = ChallengeType.objects.get(challenge_id = challengeid)
   
    challengeobj.status = "approve"
    challengeobj.save()
    
    
def hostreject(request):
    logger.debug("In hostreject")
    host = request.GET.get('host_id',None)
    
    AuthUserGroupsobj = AuthUserGroups.objects.get(id = host,group=Group.objects.get(pk=1))
    userid = AuthUserGroupsobj.user.id
    userobj = UserType.objects.get(user = userid)
   
    userobj.host_permission = "reject"
    userobj.save()
    
def challengereject(request):
    logger.debug("In challengereject")
    challenge = request.GET.get('challenge_id',None)
    #print "challenge is.........",challenge
    usergroup = UserChallengeCategoryLocationRelRel.objects.get(id = challenge)
    
    challengeid = usergroup.challenge.challenge_id
   
    challengeobj = ChallengeType.objects.get(challenge_id = challengeid)
    #print challengeobj
    challengeobj.status = "reject"
    challengeobj.save()
   # print "save done"
    

def viewchallenge(request):
    logger.debug("in view challenge")
    modelDict=[]
    challenge = request.GET.get('challenge_id',None)
    time_list=[]
    usergroup = UserChallengeImage.objects.get(id = challenge)
    usergroup0 = UserChallengeCategoryLocationRelRel.objects.get(id = challenge)
    
  
    challengeid = usergroup0.challenge.challenge_id
    print("challengeid------",challengeid)
    challenge = ChallengeType.objects.filter(pk = challengeid)
    usergroup12 = UserChallengeCategoryLocationRelRelLocation.objects.filter(userchallengecategorylocationrelrel=usergroup0)
    
    usergroup13 = UserChallengeCategoryLocationRelRelCategory.objects.filter(userchallengecategorylocationrelrel=usergroup0)
    auth_user_group_id = usergroup0.user.id
    AuthUserGroupsobj = AuthUserGroups.objects.get(id = auth_user_group_id)   
    userid = AuthUserGroupsobj.user.id
    UserTypeobj = UserType99.objects.filter(user =  userid)
    print("zxcvbnm__________",UserTypeobj)
    AuthUserobj = User.objects.get(id = userid)
    print("asdfghjk**********",AuthUserobj)
    use=[]
    cat=[]
    loc=[]
    c=[]
    user=[]
    img=[]
    category=Category.objects.filter(pk__in=[category.categorytype.pk for category in usergroup13])
    print("#########################################",category)
    for k in category :
        cat.append(model_to_dict(k))
        print("category&&&&&&&&",k)
    location=LocationType.objects.filter(pk__in=[location.locationtype.pk for location in usergroup12])
    for k in location :
       loc.append(model_to_dict(k))
       print("location**********",k)
    for k in challenge:
        c.append(model_to_dict(k)) 
    for k in UserTypeobj:
        user.append(model_to_dict(k)) 
    use.append(model_to_dict(AuthUserobj))
    img.append(model_to_dict(usergroup))
    print("&&&&",img.append(model_to_dict(usergroup)))
    challengeobj={}
    challengeobj['user']=user
    challengeobj['use']=use
    challengeobj['category']=cat
    challengeobj['location']=loc
    challengeobj['challenge']=c
    challengeobj['img']=img
    modelDict.append((challengeobj))
    print("&&&&&&&&&&&&&")    
    return JsonResponse(modelDict,safe=False)
    
def rejectChallenge(request):
    logger.debug("In rejectchallenge")
    #print"in rejectchallenge"
    challenge = request.POST.get('challenge_id')
    usergroup = UserChallengeCategoryLocationRelRel.objects.get(id = challenge)
    status = StatusType.objects.get(status = "host_decline")
    print("In rejectChallenge")
    print("user: ",FCMDevice.objects.filter(user=usergroup.user.user))
    mobile_device = FCMDevice.objects.filter(user=usergroup.user.user)
    deviceiOS = APNSDevice.objects.filter(user=usergroup.user.user)
    print("devices to which notifications is sent: ",mobile_device)
    message="Dear "+ usergroup.user.user.email+", we hearby notify you that your challenge "+usergroup.challenge.title+", has been rejected by admin team kindly get in touch with admin in case of any query. "
    mobile_device.send_message("Gifter Join Challenge ",message)
    deviceiOS.send_message(message)
    AuthUserGroupsobj = AuthUserGroups.objects.filter(pk = usergroup.user.pk,group=Group.objects.get(pk=1))
    print("###########",AuthUserGroupsobj)
    NotificationInbox.objects.create(message=message,user=AuthUserGroupsobj[0],msg_generated_date=datetime.datetime.now())
    print("message sent")  
    usergroup.status = status
    usergroup.save()    
    return redirect('/mygift/challenge/')




def approveChallenge(request):
    logger.debug("In approvechallenge")    
    challenge = request.POST.get('challenge')    
    usergroup = UserChallengeCategoryLocationRelRel.objects.get(id = challenge)
    status = StatusType.objects.get(status = "host_approve")    
    usergroup.status = status
    usergroup.save()
    print("In Approve Challenge")    
    print("user: ",FCMDevice.objects.filter(user=usergroup.user.user))
    mobile_device = FCMDevice.objects.filter(user=usergroup.user.user)
    deviceiOS = APNSDevice.objects.filter(user=usergroup.user.user)
    print("devices to which notifications is sent: ",mobile_device)
    message="Dear Host "+ usergroup.user.user.email+", Congrats.  Your challenge "+usergroup.challenge.title+" ,has been approved and available for Gifters to Join "
    mobile_device.send_message("Gifter Join Challenge ",message)
    deviceiOS.send_message(message)
    AuthUserGroupsobj = AuthUserGroups.objects.filter(pk = usergroup.user.pk,group=Group.objects.get(pk=1))
    print("###########",AuthUserGroupsobj)
    NotificationInbox.objects.create(message=message,user=AuthUserGroupsobj[0],msg_generated_date=datetime.datetime.now())
    print("message sent")    
    return redirect('/mygift/challenge/')

def viewhost(request):
#    print("#####################3")
   logger.debug("In viewhost")
   #print"in view host"
   modelDict=[]
   if request.method=='GET':
    #print "in GET method"
   
    host = request.GET.get('host_id',None)
    userobj = UserType99.objects.get(user = host)
#     print(">>>>>>>>>>>>>>",userobj)
    id=userobj.user.id
    auth1=[]
    authuserobj = User.objects.filter(id = id)
    for ll in authuserobj:
        auth1.append(model_to_dict(ll))
    
    
    print("dict",authuserobj)
    modelDict.append(model_to_dict(userobj))
    authgroup=AuthUserGroups.objects.filter(user=authuserobj,group=Group.objects.get(pk=1))
    print("$$$$$$$$$$$$$4",authgroup)
    rate=[]
    rating=HostRating.objects.filter(user=authgroup[0])
    print("host rate:-",rating)
    for aa in rating:
         rate.append(model_to_dict(aa))
    auth=[]
    auth.append(model_to_dict(userobj))
    for obj in authuserobj:
        auth.append(model_to_dict(obj))
    host={}
    host['rate']=rating[0].host_rating
#    print("rateimg:-",rating[0].host_rating)
    host['auth']=model_to_dict(userobj)
    host['auth1']=authuserobj[0].email
    print("host:-",model_to_dict(userobj))
    modelDict.append((host))
    print("all_-",modelDict.append((host)))
    
         
    return JsonResponse(modelDict,safe=False)
    
def rejectHost(request):
    logger.debug("In rejectHost")
    #print "in reject host"
    #print"host reject"
    #print"in host approve"
    host = request.POST.get('host_id')
    #print "host is.........",host
#     AuthUserGroupsobj = AuthUserGroups.objects.get(id = host)
#     userid = AuthUserGroupsobj.user.id
    userobj = UserType.objects.get(user = host)
    print("USERobj",userobj)
    #print userobj
    userobj.host_permission = "2"
    userobj.save()
    print("In rejectHost")
    print("user: ",FCMDevice.objects.filter(user=userobj.user))
    mobile_device = FCMDevice.objects.filter(user=userobj.user)
    deviceiOS = APNSDevice.objects.filter(user=userobj.user)
    print("devices to which notifications is sent: ",mobile_device)
    message="Dear Host "+ userobj.user.email+", Greetings from GIFT Team.  Your request to Host subscription has been declined.  Kindly contact us for further details (Email / Phone)"
    mobile_device.send_message("Gifter Join Challenge ",message)
    deviceiOS.send_message(message)
    AuthUserGroupsobj = AuthUserGroups.objects.filter(user = userobj.user,group=Group.objects.get(pk=1))
    print("###########",AuthUserGroupsobj)
    NotificationInbox.objects.create(message=message,user=AuthUserGroupsobj[0],msg_generated_date=datetime.datetime.now())
    print("message sent")
    
    return redirect('/mygift/host/')
    
def approveHost(request):
    logger.debug("In approveHost")
    #print"in approveHost"
    #print"in host approve"
    host = request.POST.get('host')
    #print "host is.........",host
#     AuthUserGroupsobj = AuthUserGroups.objects.get(id = host)
#     userid = AuthUserGroupsobj.user.id
    userobj = UserType.objects.get(user = host)
    #print userobj
    userobj.host_permission = "3"
    userobj.save()
    print("In Approve Host")
     
    print("user: ",FCMDevice.objects.filter(user=userobj.user))
    mobile_device = FCMDevice.objects.filter(user=userobj.user)
    deviceiOS = APNSDevice.objects.filter(user=userobj.user)
    print("devices to which notifications is sent: ",mobile_device)
    message="Dear Host "+ userobj.user.email+", Congrats.  Welcome to the Gift Platform.  Your request to Host subscription has been approved.  You can create Challenge now onwards  "
    mobile_device.send_message("Gifter Join Challenge ",message)
    deviceiOS.send_message(message)
    AuthUserGroupsobj = AuthUserGroups.objects.filter(user = userobj.user,group=Group.objects.get(pk=1))
    print("###########",AuthUserGroupsobj)
    NotificationInbox.objects.create(message=message,user=AuthUserGroupsobj[0],msg_generated_date=datetime.datetime.now())
    print("message sent")
    return redirect('/mygift/host/')

def hostname(request):
    logger.debug("In hostname")
    #print("in host name")
    modelDict=[]
    hostobj = UserType99.objects.all()
    for obj in hostobj:
        modelDict.append(model_to_dict(obj))
         
    return JsonResponse(modelDict,safe=False)

    
    
@login_required(login_url="/mygift/login/")
def gifter(request):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2")
    logger.debug("In Host")
    UserTypeForm1 = UserTypeForm()    
    context = RequestContext(request)
    authusergroup = AuthUserGroups.objects.filter(group = 2).order_by('-id')  
    print("group 22",authusergroup)  
    new_list=[]
    for obj in authusergroup:        
        userid = obj.user.id
        print("aasasas%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%",userid)
        authuser = User.objects.get(id = userid)
        print("!!!!!!!!!!!1",authuser)
        if authuser.is_active == 1:
         authuserid = authuser.id     
         usergroup = UserType99.objects.get(user = userid)  
         print("@@@@@@@@@@@@@@@###############@@@@@@@@@@@",usergroup.user)      
         new_list.append(usergroup )
        
    print("32323",new_list)
#         new_list.sort(key=lambda usergroup: usergroup.host_permission)
#         
    GiftList = UserType1(new_list)
    return render(request,"gifter_list.html", {'GiftList':GiftList,'UserTypeForm':UserTypeForm1},context)


def viewgift(request):
   print("$$$$$$$$$$$$$$$$$$$$")
   logger.debug("In viewgift")
   #print"in view host"
   modelDict=[]
   if request.method=='GET':

    host = request.GET.get('gift_id',None)

    userobj = UserType99.objects.get(user = host)   
    #print userobj
    id=userobj.user.id
    #print "id....",id
    auth1=[]
    authuserobj = User.objects.filter(id = id)
    for ll in authuserobj:
        auth1.append(model_to_dict(ll))
    print("dict",authuserobj)

    auth=[]
    auth.append(model_to_dict(userobj))
    for obj in authuserobj:
        auth.append(model_to_dict(obj))
    authgroup=AuthUserGroups.objects.filter(user=authuserobj,group=Group.objects.get(pk=2))
    print("$$$$$$$$$$$$$4",authgroup)
    rate=[]
    rating=GifterRating.objects.filter(gift_user=authgroup[0])
    for aa in rating:
         rate.append(model_to_dict(aa))
    print("Gifter rate:-",rating)
    
                
    gifter={}
    gifter['rate']=rating[0].gifter_rating
    gifter['auth']=model_to_dict(userobj)
    gifter['auth1']=authuserobj[0].email    
    modelDict.append((gifter))
    print("gifter all:-",  modelDict.append((gifter)))        
    return JsonResponse(modelDict,safe=False)

@login_required(login_url="/mygift/login/")    
def table_notification(request):
    context = RequestContext(request)   
    query=Notification.objects.all()
    #print("Count----",query)
    for k in query:
        print("Actor : ",k.actor)
        print("Verb :",k.verb)
#     aa=query.count()
    notificationlist = notificationTable(Notification.objects.all())
    return render(request,"notification_list.html", {'notificationlist':notificationlist,},context)



def viewnotification(request):
    print("in views nbhghghghgh")
    logger.debug("In viewgift")
    modelDict=[]
    if request.method=='GET':
        host = request.GET.get('notification_id',None)#         
        userobj = Notification.objects.get(id = host)
        modelDict.append(model_to_dict(userobj))
        return JsonResponse(modelDict,safe=False)


def notification(request):
    query=Notification.objects.all()
    
    return render_to_response('notification_list.html',{'query':query})



@login_required(login_url="/mygift/login/")
def mark_as_read(request, slug=None):
    print("start mark as read",request.GET.get('notification_id'))
#     notification_id = slug2id(notification_id)
    id=request.GET.get('notification_id')
    print("############",id)

    notification = get_object_or_404(
        Notification, recipient=request.user, id=id)
    notification.mark_as_read()

    _next = request.GET.get('next')

    if _next:
        return redirect(_next)

    return redirect('notifications:unread') 