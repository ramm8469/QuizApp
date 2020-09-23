from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm,CustomUserChangeForm

# Register your models here.

customUserModel = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    forms = CustomUserChangeForm
    model = customUserModel
    list_display = ['username','email']

admin.site.register(customUserModel, CustomUserAdmin )
