from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Class ,User ,Student
from .forms import ProfilePictureForm

class LoginTemplateView(TemplateView):
    template_name = "accounts/login.html"


class RegisterTemplateView(TemplateView):
    template_name = "accounts/registration.html"





class AddClassView(CreateView):
    model = Class
    fields = ['name']
    success_message = "Class Added Successfully"
    success_url = reverse_lazy('accounts:add_class')  
    template_name = 'accounts/add_class.html'



class ProfileTemplateView(TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add context data here
        context['user'] = self.request.user  # Assuming the user is authenticated
        context['student'] = Student.objects.get(user=self.request.user)
        return context
    

class EditProfileTemplateView(TemplateView):
    template_name = "accounts/edit_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_picture_form'] = ProfilePictureForm(instance=self.request.user)
        return context