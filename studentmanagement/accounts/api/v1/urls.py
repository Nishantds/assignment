# management/urls.py

from django.urls import path
from .views import GetClassView, RegisterStudentView, LoginView, UpdateProfileView

urlpatterns = [
    path('class/', GetClassView.as_view(), name='create-class'),
    path('register/', RegisterStudentView.as_view(), name='register-student'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<int:pk>', UpdateProfileView.as_view(), name='update-profile'),
   
]
