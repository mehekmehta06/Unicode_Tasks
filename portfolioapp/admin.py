from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import UserProfile

#UserProfile = get_user_model()
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('Fname','Lname','username','email')

admin.site.register(UserProfile)


