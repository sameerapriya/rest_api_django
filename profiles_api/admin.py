from django.contrib import admin
from .models import UserProfile,UserProfileManager,ProfileFeedItem
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)