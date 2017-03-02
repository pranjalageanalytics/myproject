from django import forms
from gift_app.models import *

class loginForm(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))

class ChallengeTypeForm(forms.Form):
    reg_expire_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess' , 'type':'date'}))
    direction = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control col-sm-3 viewOnlyAccess','rows':'1'}))
    photo = models.ImageField()
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    venue = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control col-sm-3 viewOnlyAccess','rows':'1'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control col-sm-3 viewOnlyAccess','rows':'1' }))
    commited_volunteers = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    requested_volunteers = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    decline_volunteers = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    tentative_volunteers = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    start_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess' , 'type':'date'}))
    end_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess' , 'type':'date'}))
    start_time = forms.CharField(required=False,widget=forms.TimeInput(attrs={'class':'col-sm-3 form-control viewOnlyAccess','type':'time',}))
    end_time = forms.CharField(required=False,widget=forms.TimeInput(attrs={'class':'col-sm-3 form-control viewOnlyAccess','type':'time',}))
    post_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess' , 'type':'date'}))
    accepted_volenteers_by_host = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    declined_volenteers_by_host = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    location = forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control viewOnlyAccess','rows':'1'}))
class CategoryLocationRelForm(forms.Form):
    category = forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control viewOnlyAccess','rows':'1'}))
    location = forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control viewOnlyAccess','rows':'1'}))
    
# class UserTypeForm(forms.Form):
#     organization = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess','rows':'1'}))
#     contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
#     website = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
#     user = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    
class  AuthUserForm(forms.Form):
    email =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))  
    
class UserTypeForm(forms.ModelForm):
    organization = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control col-sm-3 viewOnlyAccess','rows':'1'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    website = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control col-sm-3 viewOnlyAccess','rows':'1'}))
    user = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    hometown = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    date_of_birth = forms.DateField(required=False,widget=forms.DateInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess' , 'type':'date'}))
    image = models.ImageField()
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    gender=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 viewOnlyAccess'}))
    class Meta:
        model = UserType
        fields = ['organization','contact','website','user','hometown','date_of_birth','image','full_name','occupation']
        
