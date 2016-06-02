from app import serializers

from rest_framework import viewsets, mixins, status
# from rest_framework.decorators import detail_route, list_route, parser_classes  # noqa
from rest_framework.response import Response

from app import models


class CustomModelViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    pass


class ItemView(CustomModelViewSet):
    """CMS Resource"""

    def get_queryset(self):
        return models.Item.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ItemList

    def list(self, request, *args, **kwargs):
        """
        Item List
        """
        return super(ItemView, self).list(request, *args, **kwargs)
