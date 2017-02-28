from django.shortcuts import render, get_object_or_404, render_to_response, redirect

from django.views.generic import TemplateView
from django.views import generic
from django.contrib.auth import authenticate, login,logout
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.template import RequestContext
import requests,base64
from requests.auth import HTTPBasicAuth
import json
import urllib
import urllib2
from django.http import JsonResponse
import token

from django.contrib.auth import login as auth_login
import datetime
from .forms import ProfileForm,UserImageForm
from gift_app.models import UserChallengeCategoryLocationRelRel,UserType
from django.contrib.auth.models import User,Group

from rest_framework.authtoken.models import Token   
from pickle import APPEND
from django.contrib.auth.decorators import login_required


BASE_URL="http://192.168.1.129:8063/rest-auth/";
GIFT_URL="http://192.168.1.129:8063/gift/v1/";


def category_unselect(request):

    return render(request,"Home/home.html",{'email':request.session['email']})


def errorview(request):
     return render(request, "Home/404.html")
def Home(request):
    try:
        return render(request,"base.html" )
    except Exception as e:
         print("exception@@@@@",e)
         return redirect('/home/pagenotfound/')

def Save(request):
    try:
    
         url =BASE_URL+"users/2/"
         print("in save")
         
         headers = {
                         'Content-type' :"application/json",
                        
          
                    }
         
         payload = {
                 'user':{
                         'email':request.POST.get("email"),
                         'password':request.POST.get("password")
                         },
                 'display_name':request.POST.get('display_name'),
                 'alias':request.POST.get('alias'),
                 'full_name':request.POST.get('fullname'),
                 'gender': request.POST.get('gender'),
                 'hometown': request.POST.get('hometown'),
                 'occupation':request.POST.get('occupation'),
                 'date_of_birth':request.POST.get('dob'),
        #             'organization':request.POST.get('organization'),
        #             'website':request.POST.get('website'),
                 'contact':request.POST.get('contact'),
                 }
         
         print("reg_save",payload)
         display_name=request.POST.get('display_name'),
         response = requests.post(url,headers=headers,data=json.dumps(payload))
         print("hii",response)
         print(response.content)
         
         print("reg_save",response)
         print("reg_save",response.content)
        
        #  
         if response.status_code== 201:
             context1="Thank you for Registration.  We have sent a link on your registered email id.  Request you to kindly validate your registration."
             return render(request, "base.html",{'context1': context1})
         if response.status_code== 400:
             context2= "Account already exists for same user credentials"
             return render(request, "base.html",{'context2':context2})
         return render(request, "base.html",payload)
    except Exception as e:
         print("exception@@@@@",e)
         return redirect('/home/pagenotfound/')

def Host_registration(request):
    
    try:
        
        url =BASE_URL+"users/1/"
        print("Host_registration")
        
        headers = {
                        'Content-type' :"application/json",
                       
         
                   }
        
        payload = {
                'user':{
                        'email':request.POST.get("email"),
                        'password':request.POST.get("password")
                        },
    #             'display_name':request.POST.get('display_name'),
                'alias':request.POST.get('alias'),
    #             'full_name':request.POST.get('fullname'),
                'gender': request.POST.get('gender'),
                'hometown': request.POST.get('hometown'),
                'occupation':request.POST.get('occupation'),
                'date_of_birth':request.POST.get('dob'),
                'organization':request.POST.get('organization'),
                'website':request.POST.get('website'),
                'contact':request.POST.get('contact'),
                }
        
        print("Host_registration",payload)
         
        response = requests.post(url,headers=headers,data=json.dumps(payload))
        
    #     print(response.content)
        
        print("Host_registration",response)
        if response.status_code== 201:
            context1="Thank you for Registration.  We have sent a link on your registered email id.  Request you to kindly validate your registration."
            return render(request, "base.html",{'context1': context1})
        if response.status_code== 400:
            context2= "Account already exists for same user credentials"
            return render(request, "base.html",{'context2':context2})
        return render(request, "base.html",payload)
    except Exception as e:
         print("exception@@@@@",e)
         return redirect('/home/pagenotfound/') 
     
     
     
     
def gifter_update(request):
    try:
    	headers={'content-type' : 'application/json', 

			"Authorization":"Bearer"+str(request.session['name'])
		}  

    
  
    
        r = requests.get(BASE_URL+'users_update/'+str(request.session['userid'])+"/")
    
        object =r.json()
    
        gender=object.get('gender')
        response = requests.get(GIFT_URL+'getgifterrating/2/'+str(request.session['userid']))
        print("gifter_update",response.url)
        object_rating =response.json()
        print("gifter_update rating", object_rating)
    
        if request.method == 'POST':
          
            url = BASE_URL+'users_update/'+str(request.session['userid'])+"/"
            print("gifter_update")
                 
                        
            payload = {
                                 
                                'display_name':request.POST.get('display_name'),
                                'alias':request.POST.get('alias'),
                                'full_name':request.POST.get('fullname'),
                                'gender': request.POST.get('gender'),
                                'hometown': request.POST.get('hometown'),
                                'occupation':request.POST.get('occupation'),
                                'date_of_birth':request.POST.get('dob'),
                                'organization':request.POST.get('organization'),
                                'website':request.POST.get('website'),
                                'contact':request.POST.get('contact'),
      
          
                    }
                    
            print(payload)
                     
            response = requests.put(url,headers=headers,data=json.dumps(payload))
                 
            print("gifter_update response",response)
            print("gifter_update content",response.content)
           
            if response.status_code== 200:
                r = requests.get(BASE_URL+'users_update/'+str(request.session['userid'])+"/")
    
                object =r.json()
                request.session['gifter_id']=object.get('user')
                print("within update user id",request.session['userid'])
                form=UserImageForm(request.POST,request.FILES)
        	print("within post")
        	if form.is_valid():
            		print ("form valid")
            		print("gifter_id ",request.session['userid'])
            		pic=form.cleaned_data['picture']
            		print pic
            		usertype=UserType.objects.get(user=User.objects.get(pk=request.session['userid']))
            		usertype.image=pic
            		usertype.save()
		frm=UserImageForm()
                gender=object.get('gender')
                update="Your Profile has been updated successfully "
                return render(request, "Home/my_profile.html",{'object':object,'gender':gender,'update': update,'email':request.session['email'],'frm':frm})
            else:         
                return redirect('/Home/pagenotfound/')         
        else: 
           
            url = BASE_URL+'check_email/'
            print("Check Email")
               
            payload1 ={
                           
                            'email': request.session['email'],
                            'group_id':'1',
                
                }
                
            print(payload1)
                 
            response = requests.post(url,headers=headers,data=json.dumps(payload1))
             
            print("gifter_update: ",response)
            print("gifter update content : ",response.content)
            mesaage = response.json()
            print("gifter update msg : ",mesaage)
            rohi= str(mesaage.get('success'))
            print("gifter key :",rohi)
            request.session['success1'] = rohi
            frm=UserImageForm()
        return render(request,"Home/my_profile.html",{'object':object,'gender':gender,'object_rating':object_rating[0]['gifter_rating'],'host_success': request.session['success1'],'email':request.session['email'],'frm':frm}) 
    except Exception as e:
         print("exception@@@@@",e)
         return redirect('/home/pagenotfound/') 
     

def UploadProfileImage(request):
    headers =  {'content-type' : 'application/json', 
                     "Authorization":"Bearer"+str(request.session['name'])
          }
         
    print("picture view")
    if request.method=='POST':
        form=UserImageForm(request.POST,request.FILES)
        print("within post")
        if form.is_valid():
            print ("form valid")
            gifter_id= request.session['gifter_id']#form.cleaned_data['challenge_id']
            print("gifter_id ",gifter_id)
            pic=form.cleaned_data['picture']
            print pic
            usertype=UserType.objects.get(user=User.objects.get(pk=gifter_id))
            usertype.image=pic
            usertype.save()
            #return redirect('/home/host_challenges/')
    else:
              frm=UserImageForm()  
              return render(request,"Home/my_profile.html",{'frm':frm})     


@csrf_exempt     
def Gifter_login(request):
  try:
    
    if request.method=="POST":
        url = BASE_URL+'login/'
        #print("gifter_login")
        #print("IIIIINNNNN POST")
#         print("email",request.POST.get("email"))
         
        headers = {
                        'Content-type' :"application/json",
                        
                   
                   }
        payload = {
                
                'email':request.POST.get("email"),
                'password':request.POST.get("password")
                       
                  }
        email = request.POST.get("email")
        #print("email email", email)
        password = request.POST.get("password")
        #print("password password",password)
        #print("@",payload)
          
        response = requests.post(url,headers=headers,data=json.dumps(payload))
        #auth_login(request,user)
        print("************",response)
        print("kkkkkkk ",response.content)
        mesaage = response.json()
        venues1 = response.json()
                  
        print("gifter deactivate msg : ",mesaage)
        if response.status_code== 400:     
            deact=mesaage.get('non_field_errors')
            print("msg : ",deact)
            
            request.session['name'] = 'name'
            request.session['email']=email
            request.session['password']=password
            if deact[0]=="User account is disabled.":
                deactivate_msg="Kindly acctivate your account from registered Email ID"
                print("mesggggg",deactivate_msg)
                return render(request,"base.html",{'deactivate_msg':deactivate_msg})
            else:
                login1="Please use valid credentials to login"
                return render(request, "base.html",{'login': login1})
        if response.status_code== 200:
            access_token=venues1[0].get('key')
            request.session['name'] = access_token
            request.session['email']=email
            request.session['password']=password         
        
        print(" request.session['email']", request.session['email'])
        print("request.session['name']", request.session['name'])
        user = authenticate(username =email, password=password)
        if user is not None:
           if user.is_active:
              print("login")
              
              auth_login(request, user)  
        #print("venues venues venues", venues1)
        for x in venues1:
            #if x.user_id:
            if len(x)>1:
                c=0
                for myvalue1 in x.itervalues():
                    print("!!!1",myvalue1)
                    if c==0:
                        #print("222",myvalue1)
                        group=myvalue1
                        #print("group1",group)
                        request.session['group']=myvalue1
                    c=c+1
                    if c>1:
                        #print("11111",myvalue1)
                        user_id=myvalue1
                        #print("userrr_idd",myvalue1)
                        request.session['userid']=myvalue1
        print "user id :   ",user_id
        #headers={"Authorization":"Bearer "+str(request.session['name'])}   
        #r = requests.get(GIFT_URL+'gifterchallenge/2/'+str(request.session['userid']),headers=headers)
#         print("qqqq",r.url)
#         print("@@@@@",r)
        #print("$$$$",r.content)
        #object_list =json.loads(r.text)
        #print("object_list object_list",object_list)
#         print("AAAAAAAAAAAAAA", object_list)
#         print("ppp",r)
        """if not object_list:
                challenge="No challenge available"
                #print("+++",challenge)
                return render(request,"base2.html",{'email':request.session['email'],'challenge':challenge})
        """
         
    if request.session['group']==2:
            print("IN IF GROUP==2")
            headers={"Authorization":"Bearer "+str(request.session['name'])} 
            selected_location = requests.get(GIFT_URL+"user_selected_location/"+str(request.session['userid']),headers=headers)
            #print("url...",selected_location.url)
            selected_list = selected_location.json()
            #print("selct list first",selected_list)
            
            selected_cat = requests.get(GIFT_URL+"user_selected_categories/"+str(request.session['userid']),headers=headers)
            selected_list_cat = selected_cat.json()
            print("-----selected------",selected_list_cat)
            
            if not selected_list:
                print("in if")
                return render(request,"Home/home.html",{'email':request.session['email']})           
            
 		   
            else:
		"""try:
                    
                    headers={"Authorization":"Bearer"+str(request.session['name'])}
                   
                    r = requests.get(GIFT_URL+'gifterchallenge/2/'+str(request.session['userid']),headers=headers)
                    object_list =r.json()
                    if response.status_code== 200:
                        login_msg="You have logged in successfully"
                        print("!~~~LOGIN",login_msg)
                        return render(request,"Home/gifter_home.html",{'login_msg':login_msg,'object_list':object_list,'email':request.session['email']}) 
                    return render(request,"Home/gifter_home.html",{'login_msg':login_msg,'object_list':object_list,'email':request.session['email']}) 
                except Exception as e:
                    print("exception@@@@@",e);
                    return redirect('/home/pagenotfound/')"""
		
                return redirect('/home/challenge/')
    if request.session['group']==1:
	""" try:
       
            headers={'content-type' : 'application/json', 

               "Authorization":"Bearer"+str(request.session['name'])
               } 
       
            r2= requests.get(GIFT_URL+'hostchallenge/1/'+str(request.session['userid']),headers=headers)
            object_list =r2.json()
             
    #     print("AAAAAAAAAAAAAA", object_list)
            if response.status_code== 200:
                    
                     login_host="You have logged in successfully"
                     print("!~~~LOGIN HOST",login_host)
               
                     if not object_list:
                        challenge="No challenge available"
                        print("+++",challenge)
                        return render(request,"base3.html",{'login_host':login_host,'email':request.session["email"],'challenge':challenge})  
                   
                     return render(request,"Home/host_home.html",{'login_host':login_host,'object_list':object_list,'email':request.session["email"]})           
               
            return render(request,"Home/host_home.html",{'object_list':object_list,'email':request.session["email"]})         
         except Exception as e:
            print("exception@@@@@",e)
            return redirect('/home/pagenotfound/')"""
       
            
        return redirect('/home/host/')        
       
    return redirect('/home/challenge/')
  except Exception as e:
         print("exception@@@@@",e)
         return redirect('/home/pagenotfound/')

@csrf_exempt
#@login_required(login_url="/home/")
def success_gifter(request):
    try:          
        return render(request, "Home/gifter_home.html",{'email':request.session['email']})
    except Exception as e:
         print("exception@@@@@",e)
         return redirect('/home/pagenotfound/') 

@csrf_exempt
#@login_required(login_url="/home/")       
def success_host(request):        
    try:
        headers={'content-type' : 'application/json', 

   	"Authorization":"Bearer"+str(request.session['name'])
  	}  
        r2= requests.get(GIFT_URL+'hostchallenge/1/'+str(request.session['userid']),headers=headers)
        object_list =r2.json()
        print("AAAAAAAAAAAAAA", object_list)
         
        print("host_my_challenge",object_list)
        if object_list:
            for obj in object_list:
    #             print("AAAAAAAAAAAAAA", obj)
                start= obj
                cha=start['challenge']
            
                start_time=cha['start_time']
                print("start_time..........",start_time)
                
                k1=0 
                aa=start_time
                if aa:
                    print("aaaaaaaaaaaaaaaaa")
                    t1=aa.split(':')
                    print(int(t1[0]))
                    final_val=None
                    if int(t1[0])>12:
                       k1=int(t1[0])-12 
                       #print ("hours : ",k1) 
                       if abs(k1)==0:
                           final_val=str('00')+":"+str(t1[1])+":"+"PM"
                       else:
                           final_val=str(abs(k1))+":"+str(t1[1])+":"+"PM"
                    else:
                       k1=int(t1[0])
                        #print ("hours : ",k1
                       if k1==0:
                           final_val=str('00')+":"+str(t1[1])+":"+"AM"
                       else:
                           final_val=str(k1)+":"+str(t1[1])+":"+"AM"
                    print("final_val: ",final_val)
                    obj['challenge']['start_time']= final_val
                
                
                
                end_time=cha['end_time']
                print("end_time..........",end_time)
                
                k1=0 
                aa=end_time
                if aa:
                    t1=aa.split(':')
                    print(t1)
                    final_val1=None
                    if int(t1[0])>12:
                       k1=int(t1[0])-12 
                       if abs(k1)==0:
                           final_val1=str('00')+":"+str(t1[1])+":"+"PM"
                       else:
                           final_val1=str(abs(k1))+":"+str(t1[1])+":"+"PM"
                    else:
                       k1=int(t1[0])
                       if k1==0:
                           final_val1=str('00')+":"+str(t1[1])+":"+"AM"
                       else:
                           final_val1=str(k1)+":"+str(t1[1])+":"+"AM"
                       
                    print("final_val: ",final_val1)
                    obj['challenge']['end_time']= final_val1
        else:
                    challenge="No challenge available"
                    print("+++",challenge)
                    return render(request,"base3.html",{'email':request.session["email"],'challenge':challenge})         
        return render(request,"Home/host_home.html",{'object_list':object_list,'email':request.session["email"]})         
    except Exception as e:
         print("exception@@@@@",e)
         return redirect('/home/pagenotfound/')   

@csrf_exempt 
#@login_required(login_url="/home/")  
def logout(request):
    try:
        print("*********************************************************************************8")
        if request.method=="POST":
            response = requests.post(BASE_URL+'logout/')           
            print("access token1---------",request.session['name'])
            del request.session['name']
            del request.session['email']
            del request.session['password']
            if response.status_code== 200:
                    request.session.flush();
                    logout="You have successfully logout"
                    print("!~~~LOGIN OUT",logout)
                    return render(request, "base.html",{'logout':logout})
            print("access token2---------",request.session['name']) 
            user = authenticate(username =email, password=password)
            if user is not None:
               if user.is_active:
#                 print("login")
#                 logger.debug("User is active")
                
                auth_login(request, user)            
            return render(request, "base.html")
            print response 
        else:
            return render(request, "base.html")
    except Exception as e:
        print("exception@@@@@",e)
        return redirect('/home/pagenotfound/') 

#@login_required(login_url="/home/")
def location(request):        
    try:
    	 headers={"Authorization":"Bearer"+str(request.session['name'])}         
    	 r=requests.get(GIFT_URL+'location',headers=headers)
         object_list =r.json()
         locationlist = []
         for value in object_list:
           location={}
           location=value['id']        
           locationlist.append(location)
         
         selected_location = requests.get(GIFT_URL+"user_selected_location/"+str(request.session['userid']),headers=headers)
         print("location",selected_location.url)
         selected_list = selected_location.json()           
         selected_locationlist = []
         for value in selected_list:
           location={}
           location=value['id']            
           selected_locationlist.append(location)           
         list = []
         for i,j in [(i,j) for i in locationlist for j in selected_locationlist]:                
             if(i==j):
                 list.append(j)
         for k in object_list:                
          return render(request,"Home/location.html",{'object_list':object_list,'obj':list,'email':request.session['email']})
         
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')  
      
#@login_required(login_url="/home/")
def category(request):
    try:
    	 headers={"Authorization":"Bearer"+str(request.session['name'])}  
         r=requests.get(GIFT_URL+'category',headers=headers)
         object_cat_list =r.json()
        
         categorylist = []
         for value in object_cat_list:
           category={}
           category=value['category_id']
           categorylist.append(category)          
         selected_category = requests.get(GIFT_URL+"user_selected_categories/"+str(request.session['userid']),headers=headers)         
         selected_list_category = selected_category.json()         
         selected_categorylist = []
         for value in selected_list_category:
           category={}
           category=value['category_id']
           selected_categorylist.append(category)         
         category_list = []
         for i,j in [(i,j) for i in categorylist for j in selected_categorylist]:            
             if(i==j):                
                 print("category==============jjj",j)
                 category_list.append(j)       
         for j in object_cat_list:
                 return render(request,"Home/category.html",{'object_list':object_cat_list,'obj':category_list,'email':request.session['email']})
 
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')
         
@csrf_exempt
#@login_required(login_url="/home/")       
def location_save(request):         
    try:
    	 headers={"Authorization":"Bearer"+str(request.session['name'])}  
         selected = requests.get(GIFT_URL+"user_selected_location/"+str(request.session['userid']),headers=headers)
         selected_list = selected.json()
         print("-----selected location------",selected_list)
         
         if not selected_list:
             print("==blank") 
             print("In Location")
             
             r=request.POST.get('loc')
             print ("location list is",r)
             
                        
             if request.method=="POST":   
                    url = GIFT_URL+'userlocations/'
                    print("location",url)
                    headers = {
                                        'Content-type' :"application/json",
                                   }                    
                    response = requests.get(url +'?'+'locations='+str(r)+'&'+'group_id=2'+'&'+'user_id='+str(request.session['userid']),headers=headers)
                    print("$$$$$$$$$$$$$$$$ location",response.url)  
                    # print("************ location",response)
                    selected_cat = requests.get(GIFT_URL+"user_selected_categories/"+str(request.session['userid']),headers=headers)
                    selected_list_cat = selected_cat.json()
                    print("-----selected------ withi location save :",selected_list_cat)
                    if selected_list_cat: 
                        print("if selected cat within location ")
                        return redirect('/home/challenge/') 
                        
                    if not selected_list_cat: 
                        print("else condition of cat within location save ")                      
                        return render(request,"Home/home.html",{'email':request.session['email']})                         
              
         else : 
             print("===selected")
             print("In Location")
             
             r=request.POST.get('loc')
             print (" location list is",r)
             
                        
             if request.method=="POST":   
                    url = GIFT_URL+'userupdatelocations/'
                    print("location",url)                         
                    headers = {
                                'Content-type' :"application/json",
                                   }
                    response = requests.get(url +'?'+'locations='+str(r)+'&'+'group_id=2'+'&'+'user_id='+str(request.session['userid']),headers=headers,)
                    print("$$$$$$$$$$$$$$$$ location2",response.url)  
                    print("************ location2",response)
         return  render(request, "Home/category.html")              
         
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')   


@csrf_exempt 
#@login_required(login_url="/home/")        
def category_save(request):	
    try:
    	headers={"Authorization":"Bearer"+str(request.session['name']),
			 'Content-type' :"application/json",
			}        
        selected_cat = requests.get(GIFT_URL+"user_selected_categories/"+str(request.session['userid']))
        selected_list_cat = selected_cat.json()
        print("-----selected------",selected_list_cat)
        if not selected_list_cat:
            print("==blank") 
            print("In category")
           
            r=request.POST.get('cat')
            print ("list is",r)
            
            url = GIFT_URL+'usercategories/'
            print("categories",url)
            response = requests.get(url +'?'+'categories='+str(r)+'&'+'group_id=2'+'&'+'user_id='+str(request.session['userid']),headers=headers)
#             print("$$$$$$$$$$$$$$$$",response.url)  
#             print("************",response)
            selected_location = requests.get(GIFT_URL+"user_selected_location/"+str(request.session['userid']),headers=headers)
            print("url...",selected_location.url)
            selected_list = selected_location.json()
            print("selct list first",selected_list) 
            if not selected_list:
                print(" category _save in if")
                return render(request,"Home/home.html",{'email':request.session['email']}) 
            else:      
                return redirect('/home/challenge/')
        
               
        else : 
             print("===selected") 
             print("In category")
             
             r=request.POST.get('cat')
             print ("list is",r)
                            
             url = GIFT_URL+'userupdatecategories/'
             print("categories",url)
    
             headers = {
                            'Content-type' :"application/json",                               
                       }        
             response = requests.get(url +'?'+'categories='+str(r)+'&'+'group_id=2'+'&'+'user_id='+str(request.session['userid']),headers=headers)     
        return  render(request, "Home/gifter_home.html")  
        
    except Exception as e:
         print("exception@@@@@",e)
         return redirect('/home/pagenotfound/')     


def Forget_Password(request):
    try:       
        url = BASE_URL+'password/reset/'
        print("Forget_Password")    
        print("email",request.POST.get("email"))             
        headers = {
                            'Content-type' :"application/json",                       
                       }
        payload = {
                    'email':request.POST.get("email"),                         
                      }            
        print("@",payload)
              
        response = requests.post(url,headers=headers,data=json.dumps(payload))
        print("!!!",response)
        print("^^^^",response.content)
        if response.status_code== 200:
            forget_password="We have sent the link to reset your password on your given email id.  Kindly do the needful. "
            return render(request,"base.html",{'forget_password':forget_password})
        
        return render(request,"Home/forget_password.html")
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')


def reset_password_save(request):

    try:
    	headers={'Content-type' :"application/json",

		"Authorization":"Bearer"+str(request.session['name'])
		}    
        if request.method == 'POST': 
            url = BASE_URL+'password/change/'+str(request.session['userid'])
            print("reset_password_save")
                         
                        
            payload = {
                                        'old_password':request.POST.get('old_password'),
                                        'new_password1':request.POST.get('new_password1'),
                                        'new_password2':request.POST.get('new_password2'),
                              }
                            
            print(payload)
            print(request.POST.get('old_password'))             
            response = requests.post(url,headers=headers,data=json.dumps(payload))
            
            mesaage = response.json()
            print("QQQQQQ",mesaage)
            rohi= str(mesaage.get('old_password'))
            print("RRRRRRRR",rohi)  
            request.session['old1']=rohi 
            print("After session",  request.session['old1'])        
            print("&&&&&&&&&&&&&",response)
            print("^^^^",response.content)
    #         if  request.session['old1'] == "Your old password was entered incorrectly. Please enter it again":
            if response.status_code== 400:
                print("Error",response.content)
                password="Your old password was entered incorrectly. Please enter it again"
                return render(request,"Home/reset_password.html",{'password':password,'email':str(request.session['email'])})   
            if response.status_code== 200:
                password1="Your password has been change successfully .Please login"
                del request.session['name']
                del request.session['email']
                del request.session['password']
                return render(request,"base.html",{'password1':password1})
    
        else:
            return render(request,"Home/reset_password.html",{'email':str(request.session['email'])})
    except Exception as e:
         print("exception@@@@@",e)
         return redirect('/home/pagenotfound/')

def reset_password_host(request):

    try:
        headers={'Content-type' :"application/json",

        "Authorization":"Bearer"+str(request.session['name'])
        }    
        if request.method == 'POST': 
            url = BASE_URL+'password/change/'+str(request.session['userid'])
            print("reset_password_save")
                         
                        
            payload = {
                                        'old_password':request.POST.get('old_password'),
                                        'new_password1':request.POST.get('new_password1'),
                                        'new_password2':request.POST.get('new_password2'),
                              }
                            
            print(payload)
            print(request.POST.get('old_password'))             
            response = requests.post(url,headers=headers,data=json.dumps(payload))
            
            mesaage = response.json()
            print("reset_password_host",mesaage)
            rohi= str(mesaage.get('old_password'))
            print("reset_password_host",rohi)  
            request.session['old1']=rohi 
            print("After session",  request.session['old1'])        
            print("&&&&&&&&&&&&&",response)
            print("^^^^",response.content)
    #         if  request.session['old1'] == "Your old password was entered incorrectly. Please enter it again":
            if response.status_code== 400:
                print("Error",response.content)
                password="Your old password was entered incorrectly. Please enter it again"
                return render(request,"Home/reset_password_host.html",{'password':password,'email':str(request.session['email'])})   
            if response.status_code== 200:
                password1="Your password has been change successfully.Please login Again"
                del request.session['name']
                del request.session['email']
                del request.session['password']
                
                return render(request,"base.html",{'password1':password1})
    
        else:
            return render(request,"Home/reset_password_host.html",{'email':str(request.session['email'])})
    except Exception as e:
         print("exception@@@@@",e)
         return redirect('/home/pagenotfound/')


#@login_required(login_url="/home/")
def Challenge(request):   
    try:
        headers={"Authorization":"Bearer"+str(request.session['name'])}    
        r = requests.get(GIFT_URL+'gifterchallenge/2/'+str(request.session['userid']),headers=headers)
        date= datetime.date.today()
	object_list =r.json()
        
        if object_list:   
            for obj in object_list:
                #print("AAAAAAAAAAAAAA", obj)
                start= obj
                cha=start['challenge']
            
                start_time=cha['start_time']
                print("start_time..........",start_time)
                
                k1=0 
                aa=start_time
                if aa:
                    t1=aa.split(':')
                    #print(t1)
                    final_val=None
                    if int(t1[0])>12:
                       k1=int(t1[0])-12 
                       if abs(k1)==0:
                               final_val=str('00')+":"+str(t1[1])+":"+"PM"
                       else:
                               final_val=str(abs(k1))+":"+str(t1[1])+":"+"PM"
                    else:
                       k1=int(t1[0])
                       #print ("hours : ",k1) 
                       if k1==0:
                               final_val=str('00')+":"+str(t1[1])+":"+"AM"
                       else:
                               final_val=str(k1)+":"+str(t1[1])+":"+"AM"
                    print("final_val: ",final_val)
                    obj['challenge']['start_time']= final_val
                
                
                
                end_time=cha['end_time']
                print("end_time..........",end_time)
                
                k1=0 
                aa=end_time
                if aa:
                    t1=aa.split(':')
                    print(t1)
                    final_val1=None
                    if int(t1[0])>12:
                       k1=int(t1[0])-12 
                       if abs(k1)==0:
                               final_val1=str('00')+":"+str(t1[1])+":"+"PM"
                       else:
                               final_val1=str(abs(k1))+":"+str(t1[1])+":"+"PM"
                    else:
                       k1=int(t1[0])
                       if k1==0:
                               final_val1=str('00')+":"+str(t1[1])+":"+"AM"
                       else:
                               final_val1=str(k1)+":"+str(t1[1])+":"+"AM"
                    print("final_val: ",final_val1)
                    obj['challenge']['end_time']= final_val1
        else:
            challenge="No challenge available"
            print("+++",challenge)
            return render(request,"Home/gifter_home.html",{'challenge':challenge,'email':request.session['email']}) 
        
        return render(request,"Home/gifter_home.html",{'date':date,'object_list':object_list,'email':request.session['email']}) 
    except Exception as e:
         print("exception@@@@@",e);
         return redirect('/home/pagenotfound/')    
  
#@login_required(login_url="/home/")
def My_Challenge(request):   
    try:
        headers={"Authorization":"Bearer"+str(request.session['name'])}  
        r = requests.get(GIFT_URL+'gifter_mychallenge_list/'+str(request.session['userid']),headers=headers)
        date= datetime.date.today()
	object_list =r.json()
        if object_list:
        
            for obj in object_list:
    #             print("AAAAAAAAAAAAAA", obj)
                start= obj
                cha=start['user_challenge_category_location']['challenge']
            
                start_time=cha['start_time']
                print("start_time..........",start_time)
                
                k1=0 
                aa=start_time
                if aa:
                    t1=aa.split(':')
                    #print(t1)
                    final_val=None
                    if int(t1[0])>12:
                       k1=int(t1[0])-12 
                       if abs(k1)==0:
                               final_val=str('00')+":"+str(t1[1])+":"+"PM"
                       else:
                               final_val=str(abs(k1))+":"+str(t1[1])+":"+"PM"
                    else:
                       k1=int(t1[0])
                       if k1==0:
                               final_val=str('00')+":"+str(t1[1])+":"+"AM"
                       else:
                               final_val=str(k1)+":"+str(t1[1])+":"+"AM"
                    print("final_val: ",final_val)
                    obj['user_challenge_category_location']['challenge']['start_time']= final_val
                
                
                
                end_time=cha['end_time']
                print("end_time..........",end_time)
                
                k1=0 
                aa=end_time
                if aa:
                    t1=aa.split(':')
                    print(t1)
                    final_val1=None
                    if int(t1[0])>12:
                       k1=int(t1[0])-12 
                       if abs(k1)==0:
                           print ("hours : ",k1)
                           final_val1=str('00')+":"+str(t1[1])+":"+"PM"
                       else: 
                           final_val1=str(abs(k1))+":"+str(t1[1])+":"+"PM"
                    else:
                       k1=int(t1[0])
                       print ("hours : ",k1) 
                       if k1==0:
                           final_val1=str('00')+":"+str(t1[1])+":"+"AM"
                       else:
                           final_val1=str(k1)+":"+str(t1[1])+":"+"AM"
                    print("final_val: ",final_val1)
                    obj['user_challenge_category_location']['challenge']['end_time']= final_val1
                    
           
        else:
            challenge="No challenge available"
            print("+++",challenge)
            return render(request,"Home/my_challenge.html",{'challenge':challenge,'email':request.session['email']} ) 
        return render(request,"Home/my_challenge.html",{'date':date,'object_list':object_list,'email':request.session['email']} )
    except Exception as e:
         print("exception@@@@@",e)
         return redirect('/home/pagenotfound/') 



#@login_required(login_url="/home/")
def My_Goal(request):    
    goal_hours=0 
    completed_hours=0
    try:
        headers={ 'Content-type' :"application/json",
    
        "Authorization":"Bearer"+str(request.session['name'])
            }     
        r = requests.get(GIFT_URL+"getgoal/"+str(request.session['userid']),headers=headers)
        object_list =r.json()
        r1 = requests.get(GIFT_URL+"getrewards/2/"+str(request.session['userid']),headers=headers)
        print("Gifter Rewards",r1)
        obj_earn =r1.json()
        print("my goal",obj_earn)
        for value in obj_earn:
            rewards=value['rewards_point']
            print("get rewards",rewards)

        for value in object_list:
            value['goal_hours']=value['goal_hours']/60
            print("goalhours",goal_hours)
	    value['completed_hours']=value['completed_hours']/60
            print("completed_hours",completed_hours)
        
    
        for obj in object_list:
            pk={}
            pk=obj['pk']
            print("pkkkk",pk)
        print("&&&",r)    
        r = requests.get(GIFT_URL+"goalpercentage/"+str(request.session['userid']),headers=headers)
        obj_list =r.json()
        if request.method == 'POST':
           
            url =GIFT_URL+"updategoal/"+str(pk)
            print("gifter_updategoal")                         
            payload = {
                                'goal_hours':request.POST.get('goal_hours'),
                                'goal_tasks':request.POST.get('goal_tasks'),           
                    }
            
            print(payload)
                      
            response = requests.put(url,headers=headers,data=json.dumps(payload))
            object_list1 =response.json()
            print("updategoal",object_list1)
            r_after_update = requests.get(GIFT_URL+"getgoal/"+str(request.session['userid']))
    #         print("$$$$",r_after_update.content)
            object_list12 =r_after_update.json()
            print ("object_list1 :",object_list12)
            for value in object_list12:
                value['goal_hours']=value['goal_hours']/60
		value['completed_hours']=value['completed_hours']/60
                print("completed_hours",completed_hours)
            #goal_hours=0   
            #object_list1[0].=goal_hours
            print("goalhours ",object_list12)
    
    
            r_after_updatepercent = requests.get(GIFT_URL+"goalpercentage/"+str(request.session['userid']))
    #         print("eeeee",r_after_updatepercent.content)
            object_list1 =r_after_updatepercent.json()
            return render(request,"Home/my_goal.html",{'rewards':rewards,'object_list':object_list12,'obj':object_list1,'email':request.session['email']})
        
        return render(request,"Home/my_goal.html",{'rewards':rewards,'object_list':object_list,'obj':obj_list,'email':request.session['email']})
    except Exception as e:
         print("exception@@@@@",e)
         return redirect('/home/pagenotfound/') 
         
#@login_required(login_url="/home/")
def set_goal(request):    
    try:
    	headers={'Content-type' :"application/json",
		  "Authorization":"Bearer"+str(request.session['name'])
		}    
        if request.method == 'POST':
            url =GIFT_URL+"setgoal/"           
            payload = {
                           
                       'goal_hours':request.POST.get("goal_hours"),
                       'goal_tasks':request.POST.get("goal_tasks")
                                  
                         }               
            response = requests.post(GIFT_URL+"setgoal/"+str(request.session['userid']),headers=headers,data=json.dumps(payload))
            print response 
              
            object_list1 = response.json()
            r_after_update = requests.get(GIFT_URL+"getgoal/"+str(request.session['userid']))
    #         print("$$$$",r_after_update.content)
            object_list12 =r_after_update.json()
            for value in object_list12:
                value['goal_hours']=value['goal_hours']/60
            
            r1 = requests.get(GIFT_URL+"getrewards/2/"+str(request.session['userid']),headers=headers)
            print("Gifter Rewards",r1)
            obj_earn =r1.json()
            print("my goal",obj_earn)
            for value in obj_earn:
                rewards=value['rewards_point']
                print("get rewards",rewards)   

            r_after_updatepercent = requests.get(GIFT_URL+"goalpercentage/"+str(request.session['userid']))
    #         print("eeeee",r_after_updatepercent.content)
            object_list1 =r_after_updatepercent.json()
            return render(request,"Home/my_goal.html",{'rewards':rewards,'object_list':object_list12,'obj':object_list1,'email':request.session['email']})  
        return render(request,"Home/my_goal.html",{'email':request.session['email']})  
    except Exception as e:
         print("exception@@@@@",e)
         return redirect('/home/pagenotfound/') 


#@login_required(login_url="/home/")
def joinchallenge(request,pk):  
    try:
    	headers={
			  'content-type' : 'application/json',
			  "Authorization":"Bearer"+str(request.session['name'])
			}      
        url =GIFT_URL+"create_mychallenge/2/"+pk+"/"+str(request.session['userid'])                        
        payload = {
                                 
                                'status':2,  
          
                 }               
        response = requests.post(url,headers=headers,data=json.dumps(payload))                 
        print("&&&&&&&&&&&&&",response)
        r = requests.get(GIFT_URL+'gifterchallenge/2/'+str(request.session['userid']),headers=headers)
        object_list =r.json()        
        return render(request,"Home/gifter_home.html",{'object_list':object_list,'email':request.session['email']}) 
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')

#@login_required(login_url="/home/")
def acceptchallenge(request,pk):
    
    try:
    	headers={
			  'content-type' : 'application/json',
			  "Authorization":"Bearer"+str(request.session['name'])
			}      
        url =GIFT_URL+"create_mychallenge/2/"+pk+"/"+str(request.session['userid'])                        
        payload = {
                                'status':2,     
                 }                    
        response = requests.post(url,headers=headers,data=json.dumps(payload))
        print("&&&&&&&&&&&&&",response)
        r = requests.get(GIFT_URL+'gifterchallenge/2/'+str(request.session['userid']),headers=headers)
        object_list =r.json()        
        return render(request,"Home/gifter_home.html",{'object_list':object_list,'email':request.session['email']}) 
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')

#@login_required(login_url="/home/")
def rejectchallenge(request,pk):
      
    try:
    	headers={
			  'content-type' : 'application/json',
			  "Authorization":"Bearer"+str(request.session['name'])
			}  
        url =GIFT_URL+"create_mychallenge/2/"+pk+"/"+str(request.session['userid'])                
        payload = {
                                 
                                'status':4,
                  }                     
        response = requests.post(url,headers=headers,data=json.dumps(payload))
                 
        print("&&&&&&&&&&&&&",response)
        r = requests.get(GIFT_URL+'gifterchallenge/2/'+str(request.session['userid']),headers=headers)
        object_list =r.json()       
        return render(request,"Home/gifter_home.html",{'object_list':object_list,'email':request.session['email']}) 
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')

#@login_required(login_url="/home/") 
def tentativechallenge(request,pk):    
    try:
    	headers={
			  'content-type' : 'application/json',
			  "Authorization":"Bearer"+str(request.session['name'])
			}  
    
        url =GIFT_URL+"create_mychallenge/2/"+pk+"/"+str(request.session['userid'])
        print("gift tentativechallenge")
        print("urllll",url)                         
        payload = {
                                'status':5,          
                 }
                    
        print(payload)                     
        response = requests.post(url,headers=headers,data=json.dumps(payload))                 
        print("&&&&&&&&&&&&&",response)
        print("222",response.content)
        r = requests.get(GIFT_URL+'gifterchallenge/2/'+str(request.session['userid']),headers=headers)        
        print("$$$$",r.content)
        object_list =r.json()
        print("AAAAAAAAAAAAAA", object_list)        
        return render(request,"Home/gifter_home.html",{'object_list':object_list,'email':request.session['email']}) 
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')
         
         
#@login_required(login_url="/home/")         
def get_participants(request,accp_id):  
    try:
    	headers={
			  'content-type' : 'application/json',
			  "Authorization":"Bearer"+str(request.session['name'])
			}  
        r = requests.get(GIFT_URL+'accept_gifter_list_by_host/'+(accp_id)+"/"+str(request.session['userid']),headers=headers)
        obj_list =r.json() 
        return render(request,"Home/get_participants.html",{'obj_list':obj_list,'email':request.session['email'],'accp_id':accp_id} )
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')
         
         
#@login_required(login_url="/home/")        
def acceptchallengehost(request,pk,challenge_id):
   
    try:
    	headers={
			  'content-type' : 'application/json',
			  "Authorization":"Bearer"+str(request.session['name'])
			}     
        url = GIFT_URL+'gifter_acceptance_by_host/'+pk+"/"+str(request.session['userid'])
        print("Accept by host")                
        resp = requests.get(url,headers=headers)
        obj_list =resp.json()   
        user=obj_list.get("user")
        challenge=obj_list.get("challenge")                     
        payload = {                   
                    "user": user,
                     "challenge": challenge,
                     "status": 7                 
                    }                   
        response = requests.put(url,headers=headers,data=json.dumps(payload))
        print("accept",response)
    #     print(response.content)
        return redirect('/home/get_participants/'+challenge_id)
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')
         

#@login_required(login_url="/home/") 
def rejectchallengehost(request,pk,challenge_id):
    
    try:
    	headers={
			  'content-type' : 'application/json',
			  "Authorization":"Bearer"+str(request.session['name'])
			}     
        url = GIFT_URL+'gifter_acceptance_by_host/'+pk+"/"+str(request.session['userid'])
        print("Accept by host")                
        resp = requests.get(url,headers=headers)
        obj_list =resp.json()  
        user=obj_list.get("user")
        challenge=obj_list.get("challenge")     
        payload = {                  
                    "user": user,
                     "challenge": challenge,
                     "status": 3                 
                    }                     
        response = requests.put(url,headers=headers,data=json.dumps(payload))
        print("accept",response)
    #     print(response.content)
        return redirect('/home/get_participants/'+challenge_id)

    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')
    #return render(request,"Home/get_participants.html",{'obj_list':obj_list,'email':request.session['email']} )

#@login_required(login_url="/home/")
def My_Profile(request):
    try:
        return render(request,"Home/my_profile.html" )
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')

#@login_required(login_url="/home/")
def Past_Challenges(request):
    

    headers =  {'content-type' : 'application/json', 
                
                "Authorization":"Bearer"+str(request.session['name'])
                }
    
    r = requests.get(GIFT_URL+'gifter_mypastchallenge_list/'+str(request.session['userid']))
    print("qqqq",r.url)
    print("@@@@@",r)
    print("$$$$",r.content)
    obj_list =r.json()
    if not obj_list:
        challenge="No challenge available"
        print("+++",challenge)  
        return render(request,"Home/past_challenges.html",{'challenge':challenge,'email':request.session['email']})
    return render(request,"Home/past_challenges.html",{'obj_list':obj_list,'email':request.session['email']})

#@login_required(login_url="/home/")
def Favourite_Challenge(request):
   

    
    headers =  {  
                  'content-type' : 'application/json', 
                  "Authorization":"Bearer"+str(request.session['name'])
                }
    
    r = requests.get(GIFT_URL+'gifter_myfavouritechallenge_list/'+str(request.session['userid']))
    print("qqqq",r.url)
    print("@@@@@",r)
    print("$$$$",r.content)
    object_list =r.json()
    if not object_list:
        challenge="No challenge available"
        print("+++",challenge)  
        return render(request,"Home/favourite_challenge.html",{'challenge':challenge,'email':request.session['email']})   
    return render(request,"Home/favourite_challenge.html",{'object_list':object_list,'email':request.session['email']})

#@login_required(login_url="/home/") 
def Past_Challenges_Host(request):
    

    headers =  { 
                'content-type' : 'application/json', 
                 "Authorization":"Bearer"+str(request.session['name'])
                }
    
    r = requests.get(GIFT_URL+'host_pastchallenge_list/1/'+str(request.session['userid']))
    print("qqqq",r.url)
    print("@@@@@",r)
    print("$$$$",r.content)
    obj_list =r.json()
    if not obj_list:
        challenge="No challenge available"
        print("+++",challenge) 
        return render(request,"Home/past_challenges_host.html",{'challenge':challenge,'email':request.session['email']})
    return render(request,"Home/past_challenges_host.html",{'obj_list':obj_list,'email':request.session['email']})





#@login_required(login_url="/home/")
def Host_Profile(request):
    try:
        headers =  {'content-type' : 'application/json', 
                    }
        
        r = requests.get(BASE_URL+'users_update/'+str(request.session['userid'])+"/")
        print("qqqq",r.url)
        print("@@@@@@@@@@@@@@@@@@@@@@2",r)
        print("$$$$",r.content)
        object =r.json()
        print("AAAAAAAAAAAAAA", object)
        gender=object.get('gender')
        print("uuu",gender);
        response = requests.get(GIFT_URL+'gethostrating/1/'+str(request.session['userid']))
        print("host_update",response.url)
        object_rating =response.json()
        print object_rating
        print("host_update rating", object_rating)
        
        if request.method == 'POST':
          
            url = BASE_URL+'users_update/'+str(request.session['userid'])+"/"
            print("host_update")
                 
                        
            payload = {
                                 
                                'display_name':request.POST.get('display_name'),
                                'alias':request.POST.get('alias'),
                                'full_name':request.POST.get('fullname'),
                                'gender': request.POST.get('gender'),
                                'hometown': request.POST.get('hometown'),
                                'occupation':request.POST.get('occupation'),
                                'date_of_birth':request.POST.get('dob'),
                                'contact':request.POST.get('contact'),
      
          
                    }
                    
            print(payload)
                     
            response = requests.put(url,headers=headers,data=json.dumps(payload))
                 
            print("&&&&&&&&&&&&&",response)
            if response.status_code== 200:
                r = requests.get(BASE_URL+'users_update/'+str(request.session['userid'])+"/")
       
                object =r.json()
                gender=object.get('gender')
                print("uuu",gender);
                print("within update user id",request.session['userid'])
                form=UserImageForm(request.POST,request.FILES)
        	print("within post")
        	if form.is_valid():
            		print ("form valid")
            		print("gifter_id ",request.session['userid'])
            		pic=form.cleaned_data['picture']
            		print pic
            		usertype=UserType.objects.get(user=User.objects.get(pk=request.session['userid']))
            		usertype.image=pic
            		usertype.save()

		frm=UserImageForm()
                update="Your Profile has been updated successfully "
                return render(request,"Home/host_profile.html",{'update':update,'object':object,'object_rating':object_rating[0]['host_rating'],'email':request.session['email'],'gifter_success':request.session['hsuccess1'],'gender':gender,'frm':frm})
         
        else:   
            url = BASE_URL+'check_email/'
            print("Check Email")
               
            payload ={
                           
                            'email': request.session['email'],
                            'group_id':'2',
                
                }
                
            print(payload)
                 
            response = requests.post(url,headers=headers,data=json.dumps(payload))
             
            print("&&&&&&&&&&&&&",response)
            print("&&&&",response.content)
            mesaage = response.json()
            print("QQQQQQ",mesaage)
            rohi= str(mesaage.get('success'))
            print("RRRRRRRR",rohi)
            request.session['hsuccess1'] = rohi
        frm=UserImageForm() 
        return render(request,"Home/host_profile.html",{'object':object,'object_rating':object_rating[0]['host_rating'],'email':request.session['email'],'gifter_success':request.session['hsuccess1'],'gender':gender,'frm':frm})
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')
    #     return render(request,"Home/host_profile.html",{'object':object,,'email':request.session['email'],'gender':gender}) 




@csrf_exempt 
#@login_required(login_url="/home/")
def Create_Challenge(request):
         
    try:
         headers={
        'content-type' : 'application/json',
        "Authorization":"Bearer"+str(request.session['name'])
              }           
         r=requests.get(GIFT_URL+'location',headers=headers)
         object_list =r.json()   
         
         
         r=requests.get(GIFT_URL+'category',headers=headers)
         object_cat_list =r.json()  
         
         
         r=request.POST.getlist('allValues')
         print ("list location is",r)
         
         
         c=request.POST.getlist('allValues1')
         print ("list category is",c)
         
         if request.method=="POST":    
             url = GIFT_URL+'create_challenge/1/'+str(request.session['userid'])
             print("111",url)
             print("create challenge") 
             k1=0 
             start_time=  request.POST.get('start_time')
             t1=start_time.split(':')
             print("hours : ",int(t1[0]))
             print (t1[0])
             t2=t1[1].split(' ')
             print(t2[2])
             if t2[2]=='PM':
                print("within Pm")
                if int(t1[0])<12:
                    k1=int(t1[0])+12 
                    print ("hours : ",k1)
                else:
                    print("within else")
                    k1=int(t1[0])
                    print ("hours : ",k1)
             if t2[2]=='AM':
                k1=int(t1[0])
                print ("hours : ",k1)
             final_val=str(k1)+":"+str(t2[1])+":"+"00"
             print("final_val: ",final_val)
             
             k1=0 
             end_time=  request.POST.get('end_time')
             t1=end_time.split(':')
             print(t1)
             t2=t1[1].split(' ')
             print("within if",t2[1])
             if t2[2]=='PM':
                if int(t1[0])<12:
                    k1=int(t1[0])+12 
                    print ("hours : ",k1)
                else:
                     k1=int(t1[0])
                     print ("hours : ",k1)
             if t2[2]=='AM':
                k1=int(t1[0])
                print ("hours : ",k1)
             final_val1=str(k1)+":"+str(t2[1])+":"+"00"
             print("final_val: ",final_val1)
             #print time.strftime('%H:%M %d %B %Y (UTC)', int(aa)) 
             url = GIFT_URL+'create_challenge/1/'+str(request.session['userid'])
             print("111",url)
             print("create challenge")                    
             payload = {
                        'locationtype':request.POST.getlist('allValues'),
                        'categorytype':request.POST.getlist('allValues1'),
                        'challenge':{
                                     
                            'title':request.POST.get('title'),
                            'start_date':request.POST.get('start_date'),
                            'end_date':request.POST.get('end_date'),
                            'reg_expire_date': request.POST.get('reg_expire_date'),
                            'start_time': final_val,
                            'end_time':final_val1,
                            'description':request.POST.get('description'),
                            'requested_volunteers':request.POST.get('requested_volunteers'),
                            'contact_no':request.POST.get('contact_no'),
                            'venue':request.POST.get('venue'),
                            'direction':request.POST.get('direction'),
                            }                               
                   }               
             response = requests.post(url,headers=headers,data=json.dumps(payload))
         
             print("&&&&&&&&&&&&&",response)
             print("&&&&&&&&&&&&&",response.content)
             
             data = response.json()
             pk = data.get('pk')
             request.session['challenge_id']=pk 

         
         
             if response.status_code== 201:
                 modelDict={'success':'success'}
        
             if response.status_code== 400:
                 modelDict={'error':'error'}            
    #              
        
             return  JsonResponse(modelDict)
         else:
               frm=ProfileForm()  
               return render(request,"Home/create_challenge.html",{'object_list':object_list,'obj':object_cat_list,'email':request.session['email'],'frm':frm})      
         return render(request,"Home/create_challenge.html",{'object_list':object_list,'obj':object_cat_list,'email':request.session['email']})        
   
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')

#@login_required(login_url="/home/") 
def picture(request):
    headers =  {'content-type' : 'application/json', 
                     "Authorization":"Bearer"+str(request.session['name'])
          }
         
    print("picture view")
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        print("within post")
        if form.is_valid():
            print ("form valid")
            challenge_id= request.session['challenge_id']
            
            pic=form.cleaned_data['picture']
            print pic
            challenge=UserChallengeCategoryLocationRelRel.objects.get(pk=challenge_id)
            challenge.photo=pic
            challenge.save()
        return redirect('/home/host_challenges/')
    else:
              frm=ProfileForm()  
              return render(request,"Home/create_challenge.html",{'frm':frm})

#@login_required(login_url="/home/")        
def host_status(request):
    
    try:
        headers={
              'content-type' : 'application/json',
              "Authorization":"Bearer"+str(request.session['name'])
            }  

    
        r=requests.get(BASE_URL+'check_host_permission/'+str(request.session['userid']))
        obj= r.json()
        print("host_permis",obj)
        host_status= str(obj.get('message'))
        print("host_status",host_status)
        if host_status == "pending":
            print("message:", host_status)
            return render(request,"Home/host_pending.html",{'user':str(request.session['userid']),'email':request.session['email']})
        
        if host_status == "reject":
            print("message:", host_status)
            return render(request,"Home/host_rejected.html",{'user':str(request.session['userid']),'email':request.session['email']})
    
        
        if host_status == "approve":
            print("message:", host_status)
            return redirect('/home/create_challenge/')
                
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')

#@login_required(login_url="/home/")
def host_challenges(request):
   
    try:
        return render(request,"Home/host_challenge.html",{'user':str(request.session['userid']),'email':request.session['email']})
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')

#@login_required(login_url="/home/")
def FAQ(request):
    

    return render(request,"Home/faq_gifter.html",{'user':str(request.session['userid']),'email':request.session['email']})

#@login_required(login_url="/home/")
def Disclaimer(request):
    
    
    return render(request,"Home/disclaimer_gifter.html",{'user':str(request.session['userid']),'email':request.session['email']})

#@login_required(login_url="/home/")
def FAQ_host(request):
   
    return render(request,"Home/faq_host.html",{'user':str(request.session['userid']),'email':request.session['email']})

#@login_required(login_url="/home/")
def Disclaimer_host(request):
   
    
    return render(request,"Home/disclaimer_host.html",{'user':str(request.session['userid']),'email':request.session['email']})






#@login_required(login_url="/home/")
def host_toggle(request):
    try:        
        #         global success
        headers =  {'content-type' : 'application/json', 
                }
       
        url = BASE_URL+'check_email/'
        print("Check Email")
           
        payload ={
                       
                        'email': request.session['email'],
                        'group_id':'2',
            
            }
            
        print(payload)
             
        response = requests.post(url,headers=headers,data=json.dumps(payload))
         
        print("&&&&&&&&&&&&&",response)
        print("&&&&",response.content)
        mesaage = response.json()
        print("QQQQQQ",mesaage)
        rohi= str(mesaage.get('success'))
        print("RRRRRRRR",rohi)
        request.session['success1'] = rohi
        
        print("~~",  request.session['success1'])
        
        if request.session['success1'] == "Success":
            print("message:", request.session['success1'])
            return render(request, "Home/my_profile.html",{'host_success':request.session['success1'],'email':request.session['email']})
        
        else:
            print("in else")
            #return render(request, "Home/host_home.html",{'email':request.session['email']})
            return redirect('/home/host/') 
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')

#@login_required(login_url="/home/")
def host_toggle_save(request):            
    try:
#         email=request.session['email']
#         password=request.session['password']
        headers =  {'content-type' : 'application/json', 
                "Authorization":"Bearer"+str(request.session['name'])
                }
    
        url =BASE_URL+'usertoggle/1/'+str(request.session['userid'])
        print("in  host toggle save",url)
        print("organization : ",request.POST.get('organization'));
        print("website : ",request.POST.get('website'));
        
        if request.method == 'POST':
            
                 payload = {
#                 'user':{
#                         'email':request.session['email'],
#                         'password':   request.session['password']
#                         },               
                'organization':request.POST.get('organization'),
                'website':request.POST.get('website'),               
                }        
                 print("host_toggle_save",payload)
                 
                 response = requests.post(url,headers=headers,data=json.dumps(payload))
                 print("host_toggle_save",response)
                 return redirect('/home/host/') 
    
        return render(request, "Home/host_toggle.html",{'email':request.session['email']} ) 
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')

#@login_required(login_url="/home/")
def gifter_toggle(request):
    try:      
        email=request.session['email']
        password=request.session['password']        
        headers={ "Authorization":"Bearer "+str(request.session['name']),
                             'content-type' : 'application/json', 
                    }         
        url = BASE_URL+'check_email/'
        print("Check Email")
             
        payload ={                        
                       'email': request.session['email'],
                        'group_id':'2',              
            }              
        print(payload)
               
        response = requests.post(url,headers=headers,data=json.dumps(payload))
           
        print("&&&&&&&&&&&&&",response)
#         print("&&&&",response.content)
        mesaage = response.json()
        success= str(mesaage.get('success'))        
        request.session['hsuccess1'] = success        
        print("gifter session",  request.session['hsuccess1'])         
        if request.session['hsuccess1'] == "Success":
            print("message:", request.session['hsuccess1'])
            url =BASE_URL+"usertoggle/2/"+str(request.session['userid'])
            print("in save")      
            headers = {
                    'Content-type' :"application/json",       
               }      
            payload = {
#             'user':{
#                     'email':request.session['email'],
#                     'password':   request.session['password']
#                     },              
            }      
            print("@gifter",payload)                
            response = requests.post(url,headers=headers,data=json.dumps(payload),auth=(str(email),password))
            print("gifter",response)          
        selected_location = requests.get(GIFT_URL+"user_selected_location/"+str(request.session['userid']),headers=headers)     
        selected_list = selected_location.json()
        print("selct list first",selected_list)        
        selected_cat = requests.get(GIFT_URL+"user_selected_categories/"+str(request.session['userid']),headers=headers)
        selected_list_cat = selected_cat.json()
        print("-----selected------",selected_list_cat)            
        if not selected_list: 
                print("else in ") 
                print("if in category") 
                return render(request,"Home/home.html",{'email':request.session['email']})                     
        elif not selected_list_cat:
                print("in if")
                return render(request,"Home/home.html",{'email':request.session['email']})      
        return redirect('/home/challenge')
       # return render(request, "Home/gifter_home.html",{'email':request.session['email']})
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')

#@login_required(login_url="/home/")
@csrf_exempt
def challenge_update(request,pk):
    try:
         headers =  {'content-type' : 'application/json', 
                         "Authorization":"Bearer"+str(request.session['name'])
              }
         r=requests.get(GIFT_URL+'location',headers=headers)
         object_list =r.json() 
         r=request.POST.getlist('allValues')
         #print ("list location is",r)
             
         r=requests.get(GIFT_URL+'category',headers=headers)
         object_cat_list =r.json()  
         #print ("list location is",object_cat_list) 
         
         c=request.POST.getlist('allValues1')
         #print ("list category is",c)
         start_time=None
         end_time=None         
         r= requests.get(GIFT_URL+'update_challenge/'+pk+"/"+"1")    
         #print("update_challenge",r)
         data =r.json()
         #print "object_list[0]",data
         k1=0 
         aa=data['challenge']['start_time']
         if aa:
            t1=aa.split(':')
            #print(t1)
            final_val=None
            if int(t1[0])>12:
               k1=int(t1[0])-12 
               if abs(k1)==0:
                       final_val=str('00')+":"+str(t1[1])+":"+"PM"
               else:
                       final_val=str(abs(k1))+":"+str(t1[1])+":""PM"
            else:
               k1=int(t1[0])
               if k1==0:
                       final_val=str('00')+":"+str(t1[1])+":"+"AM"
               else:
                       final_val=str(k1)+":"+str(t1[1])+":"+"AM"
            #print("final_val: ",final_val)
            data['challenge']['start_time']= final_val
         start_time=final_val
        
        
         end_time=data['challenge']['end_time']
         #print("end_time..........",end_time)
         k1=0 
         aa=end_time
         if aa:
            t1=aa.split(':')
            #print(t1)
            final_val1=None
            if int(t1[0])>12:
               k1=int(t1[0])-12 
               if abs(k1)==0:
                   #print ("hours : ",k1)
                   final_val1=str('00')+":"+str(t1[1])+":"+"PM"
               else: 
                   final_val1=str(abs(k1))+":"+str(t1[1])+":"+"PM"
            else:
               k1=int(t1[0])
               if k1==0:
                   #print ("hours : ",k1) 
                   final_val1=str('00')+":"+str(t1[1])+":"+"AM"
               else:
                   final_val1=str(k1)+":"+str(t1[1])+":"+"AM"
            #print("final_val: ",final_val1)
         data['challenge']['end_time']= final_val1
         end_time=final_val1
         #print("update_challenge",data)
         
         
         if request.method=="POST":
             print("start_time original ",start_time)
             print("start_time update ",request.POST.get('start_time'))
             if request.POST.get('start_time')!=start_time:
                 k1=0 
                 start_time1=  request.POST.get('start_time')
                 print("within update start_time : ",start_time1)
                 t1=start_time1.split(':')
                 print("hours : ",int(t1[0]))
                 print (t1[0])
                 t2=t1[1].split(' ')
                 print(t2[2])
                 if t2[2]=='PM':
                    print("within Pm")
                    if int(t1[0])<12:
                        k1=int(t1[0])+12 
                        print ("hours : ",k1)
                    else:
                        print("within else")
                        k1=int(t1[0])
                        print ("hours : ",k1)
                 if t2[2]=='AM':
                    k1=int(t1[0])
                    print ("hours : ",k1)
                 final_val=str(k1)+":"+str(t2[1])+":"+"00"
                 print("final_val: ",final_val)
             else:
                 k1=0 
                 start_time1=  request.POST.get('start_time')
                 print("within update else start_time : ",start_time1)
                 t1=start_time1.split(':')
                 print("hours : ",int(t1[0]))
                 print (t1)
                 if t1[2]=='PM':
                    print("within Pm")
                    if int(t1[0])<12:
                        k1=int(t1[0])+12 
                        print ("hours : ",k1)
                    else:
                        print("within else")
                        k1=int(t1[0])
                        print ("hours : ",k1)
                 if t1[2]=='AM':
                    k1=int(t1[0])
                    print ("hours : ",k1)
                 final_val=str(k1)+":"+str(t1[1])+":"+"00"
                 print("final_val: ",final_val)
             if request.POST.get('end_time')!=end_time:
                 k1=0 
                 end_time=  request.POST.get('end_time')
                 print("within update end_time : ",end_time)
                 t1=end_time.split(':')
                 print(t1)
                 t2=t1[1].split(' ')
                 print("within if",t2[1])
                 if t2[2]=='PM':
                    if int(t1[0])<12:
                        k1=int(t1[0])+12 
                        print ("hours : ",k1)
                    else:
                         k1=int(t1[0])
                         print ("hours : ",k1)
                 if t2[2]=='AM':
                    k1=int(t1[0])
                    print ("hours : ",k1)
                 final_val1=str(k1)+":"+str(t2[1])+":"+"00"
             else:
                 k1=0 
                 end_time=  request.POST.get('end_time')
                 print("within update end_time : ",end_time)
                 t1=end_time.split(':')
                 if t1[2]=='PM':
                    if int(t1[0])<12:
                        k1=int(t1[0])+12 
                        print ("hours : ",k1)
                    else:
                         k1=int(t1[0])
                         print ("hours : ",k1)
                 if t1[2]=='AM':
                    k1=int(t1[0])
                    print ("hours : ",k1)
                 final_val1=str(k1)+":"+str(t1[1])+":"+"00"   
             url = GIFT_URL+'update_challenge/'+pk+"/"+"1"
             payload = {
                            'locationtype':request.POST.getlist('allValues'),
                            'categorytype':request.POST.getlist('allValues1'),
                            'challenge':{                                           
                                'title':request.POST.get('title'),
                                'start_date':request.POST.get('start_date'),
                                'end_date':request.POST.get('end_date'),
                                'reg_expire_date': request.POST.get('reg_expire_date'),
                                'start_time': final_val,
                                'end_time':final_val1,
                                'description':request.POST.get('description'),
                                'requested_volunteers':request.POST.get('requested_volunteers'),
                                'contact_no':request.POST.get('contact_no'),
                                'venue':request.POST.get('venue'),
                                'direction':request.POST.get('direction'),
                                },
                }                   
             print("PAYOAD",payload)                   
             response = requests.put(url,headers=headers,data=json.dumps(payload))
             
             print("&&&&&&&&&&&&&",response)
             print("&&&&&&&&&&&&&",response.content)
             modelDict={'success':'success'}
	     data = response.json()
             pk = data.get('pk')
             request.session['challenge_id']=pk 
	     return  JsonResponse(response)

             #return redirect('/home/host/') 
         else:
		frm=ProfileForm()
         	frm.photo=data['photo']     
         return render(request,"Home/update_challenge.html",{'object_list':object_list,'obj':object_cat_list,'data':data,'email':request.session['email'],'pk':pk,'frm':frm})
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')


#@login_required(login_url="/home/")
def host_inbox(request):
     
    headers =  {'content-type' : 'application/json', 
                "Authorization":"Bearer"+str(request.session['name'])
                }
    
    r = requests.get(GIFT_URL+'getHostNotification/'+str(request.session['userid']))
    print("host inbox",r.url)
    print("host inbox",r)
    print("host inbox.........",r.content)
    object =r.json()
    
    return render(request,"Home/inbox_host.html",{'object':object,'user':str(request.session['userid']),'email':request.session['email']})

#@login_required(login_url="/home/")
def gifter_inbox(request):
     
    headers =  {'content-type' : 'application/json', 
                "Authorization":"Bearer"+str(request.session['name'])
                }
    
    r = requests.get(GIFT_URL+'getGifterNotification/'+str(request.session['userid']))
    print("gifter inbox",r.url)
    print("gifter inbox",r)
    print("gifter inbox.........",r.content)
    object =r.json()
    
    return render(request,"Home/inbox_gifter.html",{'object':object,'user':str(request.session['userid']),'email':request.session['email']})

#@login_required(login_url="/home/")
def favouritechallenge(request,pk):
    
    try:
        headers={
              'content-type' : 'application/json',
              "Authorization":"Bearer"+str(request.session['name'])
            }      
        url =GIFT_URL+"makefavourite/2/"+pk+"/"+str(request.session['userid'])                        
        payload = {
                                'is_favourite':1,     
                 }                    
        response = requests.post(url,headers=headers,data=json.dumps(payload))
        print("favourite",response)
        r = requests.get(GIFT_URL+'gifter_mychallenge_list/'+str(request.session['userid']),headers=headers)
        object_list =r.json()        
        return render(request,"Home/my_challenge.html",{'object_list':object_list,'email':request.session['email']} ) 
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')


#@login_required(login_url="/home/")
def unfavouritechallenge(request,pk):
    
    try:
        headers={
              'content-type' : 'application/json',
              "Authorization":"Bearer"+str(request.session['name'])
            }      
        url =GIFT_URL+"makefavourite/2/"+pk+"/"+str(request.session['userid'])                        
        payload = {
                                'is_favourite':2,     
                 }                    
        response = requests.post(url,headers=headers,data=json.dumps(payload))
        print("favourite",response)
        r = requests.get(GIFT_URL+'gifter_myfavouritechallenge_list/'+str(request.session['userid']),headers=headers)
        object_list =r.json() 
        if not object_list:
            challenge="No challenge available"
            print("+++",challenge)  
            return render(request,"Home/favourite_challenge.html",{'challenge':challenge,'email':request.session['email']})       
        return render(request,"Home/favourite_challenge.html",{'object_list':object_list,'email':request.session['email']}) 
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')


#@login_required(login_url="/home/")
def gifter_ranking(request):
    
    headers =  {'content-type' : 'application/json', 
                "Authorization":"Bearer"+str(request.session['name'])
                }
    
    r = requests.get(GIFT_URL+'getgifterranking/'+str(request.session['userid']))
    print("gifter_ranking",r.url)
    print("gifter_ranking",r)
    
    object =r.json()
    print("gifter_ranking.........",object)

    return render(request,"Home/gifter_ranking.html",{'object':object,'user':str(request.session['userid']),'email':request.session['email']})

#@login_required(login_url="/home/")
def host_ranking(request):
    
    headers =  {'content-type' : 'application/json', 
                "Authorization":"Bearer"+str(request.session['name'])
                }
    
    r = requests.get(GIFT_URL+'gethostranking/'+str(request.session['userid']))
    print("host_ranking",r.url)
    print("host_ranking",r)
    
    object =r.json()
    print("host_ranking.........",object)

    return render(request,"Home/host_ranking.html",{'object':object,'user':str(request.session['userid']),'email':request.session['email']})



@csrf_exempt
#@login_required(login_url="/home/")
def gifterfeedbackchallenge(request,pk):
    
    try:
        headers={
              'content-type' : 'application/json',
              "Authorization":"Bearer"+str(request.session['name'])
            }      
        value= request.POST.get('feedbackvalue')
        print("gifterfeedbackchallenge",value)
        url =GIFT_URL+"sethostfeedback/"+pk+"/"+str(request.session['userid'])                        
        payload = {
                                'point':request.POST.get('feedbackvalue'),     
                 }                    
        response = requests.post(url,headers=headers,data=json.dumps(payload))
        print("gifterfeedback",response)
        #print("gifterfeedback",response.content)
        object_list =response.json()        
        return redirect('/home/past_challenges/')
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')   
         
#@login_required(login_url="/home/")
def checkhostfeedback(request,accp_id):
    
    try:
        headers={
              'content-type' : 'application/json',
              "Authorization":"Bearer"+str(request.session['name'])
            }      
       
        url =GIFT_URL+"checkhostfeedback/"+accp_id+"/"+str(request.session['userid'])                        
        val=None                   
        response = requests.get(url,headers=headers)
        print("checkhostfeedback",response)
        print("checkhostfeedback",response.content)
        object_list =response.json()
        #print("---",object_list)
        for i in object_list:
            #print("*******",i)
            for key,value in i.iteritems():
               # print("key=",key," value=",value)
                val=value
        print(val)
        modelDict={'val':val}
        print(modelDict)               
        return  JsonResponse(modelDict)
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/') 
         
#@login_required(login_url="/home/")
def checkgifterfeedback(request, ch_id, accp_id):
    print("innnnn")
    try:
        headers={
              'content-type' : 'application/json',
              "Authorization":"Bearer"+str(request.session['name'])
            }      
       
        url =GIFT_URL+"checkgifterfeedback/"+ch_id+"/"+accp_id                        
        val=None
        print(url)            
        response = requests.get(url,headers=headers)
        print("checkgifterfeedback",response)
        print("checkgifterfeedback",response.content)
        object_list =response.json()
        print("---",object_list)
        for i in object_list:
            #print("*******",i)
            for key,value in i.iteritems():
               # print("key=",key," value=",value)
                val=value
        print(val)
        modelDict={'val':val}
        print(modelDict)               
        return  JsonResponse(modelDict)
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')      
              


#@login_required(login_url="/home/")
def getchallengecompletedlist(request,accp_id):
    
    try:
        headers={
              'content-type' : 'application/json',
              "Authorization":"Bearer"+str(request.session['name'])
            }      
        url =GIFT_URL+"getchallengecompletedlist/"+(accp_id)+"/"+str(request.session['userid'])                        
        print(url)               
        response = requests.get(url,headers=headers)
        print("getchallengecompletedlist",response)
        print("getchallengecompletedlist....",response.content)
        obj_list =response.json() 
        print("getchallengecompletedlist",obj_list)       
        return render(request,"Home/get_challengecompletelist.html",{'obj_list':obj_list,'email':request.session['email'],'accp_id':accp_id} )
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')      

@csrf_exempt         
#@login_required(login_url="/home/")
def hostfeedbackchallenge(request,pk,ch_id):
    
    try:
        headers={
              'content-type' : 'application/json',
              "Authorization":"Bearer"+str(request.session['name'])
            }      
        url =GIFT_URL+"setgifterfeedback/"+pk+"/"+ch_id 
        print(url)    
        value=request.POST.get('feedbackvalue'),
            
        print("hostfeedbackchallenge",value)               
        payload = {
                                'point':request.POST.get('feedbackvalue'),     
                 }                    
        response = requests.post(url,headers=headers,data=json.dumps(payload))
        print("hostfeedback",response)
        #print("hostfeedback....",response.text)
        object_list =response.json() 
        print("hostfeedback",object_list)       
        return redirect('/home/past_challenges_host/')
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')                 



@csrf_exempt         
def fblogin(request):
    try:
    
        if request.method=="POST":
            url = BASE_URL+'facebook/'
            r=request.POST.get('fbemail'),
            print("fbemail",r)
            for value in r:
                 email=str(value)
            print("fbemail",email)
            headers = {
                            'Content-type' :"application/json",
                            
                       
                       }
            payload = {
                    
                    'access_token':request.POST.get("fbtoken"),
                   
                           
                      }
           
              
            response = requests.post(url,headers=headers,data=json.dumps(payload))
          
            print("facebook_login",response)
            print("facebook_login",response.content)
            fbvalue = response.json()
            
            if response.status_code== 200:
                access_token=fbvalue[0].get('key')
                request.session['name'] = access_token
                print("name", request.session['name'])
                request.session['email'] = email                
                
            for x in fbvalue:
            #if x.user_id:
                if len(x)>1:
                    c=0
                    for myvalue1 in x.itervalues():
                        print("!!!1",myvalue1)
                        if c==0:
                            #print("222",myvalue1)
                            group=myvalue1
                            #print("group1",group)
                            request.session['group']=myvalue1
                        c=c+1
                        if c>1:
                            #print("11111",myvalue1)
                            user_id=myvalue1
                            #print("userrr_idd",myvalue1)
                            request.session['userid']=myvalue1
                            print "user id :   ",user_id    
                
            if request.session['group']==2:
                print("IN IF GROUP==2")
                headers={"Authorization":"Bearer "+str(request.session['name'])} 
                selected_location = requests.get(GIFT_URL+"user_selected_location/"+str(request.session['userid']),headers=headers)
                print("url...",selected_location.url)
                selected_list = selected_location.json()
                print("selct list first",selected_list)
                
                selected_cat = requests.get(GIFT_URL+"user_selected_categories/"+str(request.session['userid']),headers=headers)
                selected_list_cat = selected_cat.json()
                print("-----selected------",selected_list_cat)
                modelDict={'selectlist':selected_list_cat}
                print(modelDict)               
                return  JsonResponse(modelDict)
 
    
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')                 

@csrf_exempt         
def googlelogin(request):
    try:
    
        if request.method=="POST":
            url = BASE_URL+'google/'
            token=request.POST.get("id_token"),
            r=request.POST.get("Email"),
            for value in r:
                 email=str(value)
            print("fbemail",email)
            headers = {
                            'Content-type' :"application/json",
                            
                       
                       }
            payload = {
                    
                    'access_token':request.POST.get("id_token"),
                   
                           
                      }
           
              
            response = requests.post(url,headers=headers,data=json.dumps(payload))
          
            print("google_login",response)
            print("google_login",response.content)
            fbvalue = response.json()
            if response.status_code== 200:
                access_token=fbvalue[0].get('key')
                request.session['name'] = access_token
                request.session['email'] = email  
                
            for x in fbvalue:
            #if x.user_id:
                if len(x)>1:
                    c=0
                    for myvalue1 in x.itervalues():
                        print("!!!1",myvalue1)
                        if c==0:
                            #print("222",myvalue1)
                            group=myvalue1
                            #print("group1",group)
                            request.session['group']=myvalue1
                        c=c+1
                        if c>1:
                            #print("11111",myvalue1)
                            user_id=myvalue1
                            #print("userrr_idd",myvalue1)
                            request.session['userid']=myvalue1
                            print "user id :   ",user_id    
                
                if request.session['group']==2:
                    print("IN IF GROUP==2")
                    headers={"Authorization":"Bearer "+str(request.session['name'])} 
                    selected_location = requests.get(GIFT_URL+"user_selected_location/"+str(request.session['userid']),headers=headers)
                    print("url...",selected_location.url)
                    selected_list = selected_location.json()
                    print("selct list first",selected_list)
                    
                    selected_cat = requests.get(GIFT_URL+"user_selected_categories/"+str(request.session['userid']),headers=headers)
                    selected_list_cat = selected_cat.json()
                    print("-----selected------",selected_list_cat)
                    modelDict={'selectlist':selected_list_cat}
                    print(modelDict)               
                    return  JsonResponse(modelDict)
    
    except Exception as e:
             print("exception@@@@@",e)
             return redirect('/home/pagenotfound/')                 
             