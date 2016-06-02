
from rest_framework import serializers
from app import models


class ItemList(serializers.ModelSerializer):

    class Meta:
        model = models.Item
        fields = ('id', 'name', 'description')
