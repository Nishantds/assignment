from django.contrib import admin
from .forms import StudentForm
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Student , User
from django.utils.html import format_html
from django.urls import reverse

def activate_users(modeladmin, request, queryset):
    queryset.update(is_active=True)
activate_users.short_description = "Activate selected users"

def deactivate_users(modeladmin, request, queryset):
    queryset.update(is_active=False)
deactivate_users.short_description = "Deactivate selected users"

# @admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name','phone', 'is_active')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups')
    actions = [activate_users, deactivate_users]

   
# Unregister the default User admin and register the custom one

admin.site.register(User,CustomUserAdmin)
admin.site.register(Student)


# Unregister the default User admin and register the custom one
# admin.site.unregister(User)
