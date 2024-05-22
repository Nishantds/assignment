# python imports

# django imports
from django.urls import path, include

# third-party imports

# inter-app imports

# local imports

# app name
from .views import (
    LoginTemplateView,
     RegisterTemplateView,
     AddClassView,
     ProfileTemplateView,
     EditProfileTemplateView

    )


app_name = 'accounts'

urlpatterns = [
    # api urls
    path('api/', include('accounts.api.urls')),
    path('login/', LoginTemplateView.as_view(), name='login'),
    path('registration/', RegisterTemplateView.as_view(), name='registration'),
    path('add-class/', AddClassView.as_view(), name='add_class'),
    path('profile/', ProfileTemplateView.as_view(), name='profile'),
    path('edit-profile/', EditProfileTemplateView.as_view(), name='editprofile')

    
    

]