from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from petstagram.accounts.models import UserProfile 

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': 'Хэрэглэгчийн нэр',
            'email': 'И-мэйл',
            'first_name': 'Нэр',
            'last_name': 'Овог',
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'gender']  # Чиний profile-д байгаа талбарууд
        labels = {
            'profile_picture': 'Профайл зураг',
            'gender': 'Хүйс',
        }