from django import forms
class ProfileForm(forms.Form):
    challenge_id=forms.IntegerField(required=False)
    picture = forms.FileField()

class UserImageForm(forms.Form):
    picture = forms.FileField()

   
   
def __init__(self, args, *kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)
    self.fields['picture'].widget.attrs={
            'class': 'form-control1 fsize',}

