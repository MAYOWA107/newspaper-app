from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'username', 'age', 'is_staff',]


admin.site.register(CustomUser, CustomUserAdmin)
