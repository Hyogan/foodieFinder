from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserRegisterForm(UserCreationForm) :
    input_classes = "bg-transparent text-white px-2 border-b-4 w-full sm:w-2/3 my-4  px-4 border-orange-600"
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "username", "class" : f"{input_classes}"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder" : "Email adress", "class" : f"{input_classes}" }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Password", "class" : f"{input_classes}"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Password confirmation", "class" : f"{input_classes}"}))

    class Meta :
        model = User
        fields = ['username','email']