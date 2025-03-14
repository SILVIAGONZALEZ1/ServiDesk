from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'role']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)