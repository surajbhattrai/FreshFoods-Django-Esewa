from django.contrib import admin
from .models import Account, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
# Register your models here.

class AccountManager(UserAdmin):
    list_display = ['first_name','last_name','username','email','last_login']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
        


class UserProfileManager(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%">'.format(object.profile_pic.url))
    thumbnail.shot_description = "Profile Pic"    
    list_display = ['thumbnail','user', 'city', 'state', 'country',]


admin.site.register(Account, AccountManager)
admin.site.register(UserProfile, UserProfileManager)