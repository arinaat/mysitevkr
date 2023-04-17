from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .models import User


# class AccountAdmin(UserAdmin):
# list_display = ('email', 'username', 'is_admin', 'is_staff')
# search_fields = ('email', 'username',)

# filter_horizontal = ()
# list_filter = ()
# fieldsets = ()


# admin.site.register(User, AccountAdmin)

@admin.register(User)
class ModelAdmin(admin.ModelAdmin):
    pass
