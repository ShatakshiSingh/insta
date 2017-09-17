from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from main.models import Post


class SignUp(UserCreationForm):
    first_name=forms.CharField(help_text="optional")
    last_name=forms.CharField(help_text = "optional")
    email=forms.EmailField(help_text = "must be valid")
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password1','password2')

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','text','image']
