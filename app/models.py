from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.URLField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True,
                                verbose_name='Phone Number')
    address = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        return self.user.username
