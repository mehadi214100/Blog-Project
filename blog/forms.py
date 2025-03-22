from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(Register,self).__init__(*args, **kwargs)

        for fieldname in self.fields:
           self.fields[fieldname].help_text = None
    

class Login(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'
