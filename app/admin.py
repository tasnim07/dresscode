from django.contrib import admin

from app.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'avatar', 'address']
    search_fields = ['user']


admin.site.register(UserProfile, UserProfileAdmin)
