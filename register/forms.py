from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(UserCreationForm):
    # email = forms.EmailField()
    email = forms.EmailField(required=True)
    # first_name = forms.CharField(max_length=30)
    # last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'username' , 'email' , 'password1' , 'password2']

    def save(self, commit=True):
        # user = super(RegisterForm, self).save(commit=False)
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ( 'age' , 'occupation' ,)

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #
    #     user.age = self.cleaned_data['age']
    #     user.location = self.cleaned_data['location']
    #     user.occupation = self.cleaned_data['occupation']

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name' , 'last_name' , 'email', 'password')

class EditProfileFormCustme(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ('first_name' , 'last_name' , 'age' , 'occupation' ,)
