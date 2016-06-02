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


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    published_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey('Category', related_name='items')
    brand = models.ForeignKey('Brand', null=True, related_name='items')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


class Cart(models.Model):
    item = models.ForeignKey('Item', related_name='carts')
    user = models.ForeignKey('UserProfile', related_name='carts')

    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return '--'.join([self.item.name, self.user.username])
