from django import forms
from .models import Profile
from django.contrib.auth.forms import UserChangeForm


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'credit', 'image']
        # exclude is used to display all fields instead the field inside that:
        # exclude = ('image')


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email')
    password = None


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label="نام", max_length=100)
    last_name = forms.CharField(label="نام خانوادگی", max_length=100)
    username = forms.CharField(label="نام کاربری", max_length=100)
    email = forms.CharField(label="سامانه الکترونیکی", widget=forms.EmailInput)
    password = forms.CharField(label="رمز ورود", widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['gender', 'credit', 'image']
