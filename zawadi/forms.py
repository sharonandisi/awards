from django import forms

class NewImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        exclude = ['profile']
        widgets = {
            ''
        }

class ProfileForm(forms.ModelForm)

    class Meta:
        model = Profile
        exclude = ['user']

class ImageUpload(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date', 'profile']

class profileEdit(forms.Form):
    name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    Bio = forms.Textarea()
    Email = forms.EmailField()
    phone_number = forms.CharField(max_length=12)
    