from django import forms
from userauths.models import User
from django.contrib.auth.forms import UserCreationForm
from userauths.models import Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}), max_length=50, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name',
            'bio',
            'profile_image', 
            'facebook', 
            'twitter', 
            'instagram',
            'country',
            'address',
            'phone',
            'website',

            ]

class userUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username', 'class': 'prompt srch_explore'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email', 'class': 'prompt srch_explore'}))

    class Meta:
        model = User
        fields = ['username', 'email']
