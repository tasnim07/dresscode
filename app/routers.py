from rest_framework import routers
from app import apis


router = routers.SimpleRouter()
router.register(r'items', apis.ItemView, 'item')
