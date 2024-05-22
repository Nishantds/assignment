# forms.py
from django import forms
from .models import Class , User

class ClassNameForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']




class StudentForm(forms.ModelForm):

    class Meta :

        model = User
        fields =(
            "first_name",
            "last_name",
            "email",
            "phone",
            "is_active"
        )





class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('image',)