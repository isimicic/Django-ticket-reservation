from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import User_profile


class UserProfileInline(admin.StackedInline):
    model = User_profile
    can_delete = False
    verbose_name_plural = 'Profile'
    list_display = ('image_thumbnail',)


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
