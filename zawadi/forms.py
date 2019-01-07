from django import forms
from .models import Image, Review, Profile

class NewImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        exclude = ['user', 'pub_date']
        widgets = {
            ''
        }

class UpdateProfile(forms.ModelForm)

    class Meta:
        model = Profile
        exclude = ['user']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
