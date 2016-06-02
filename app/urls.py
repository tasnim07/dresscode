from django.conf.urls import url, include
from app import views, routers


urlpatterns = [
    # Social user post authentication callback
    url(r'^callback/$',
        views.post_auth_callback, name='callback'),
    url(r'^login/$', views.facebook_login, name='login'),
    url(r'^logout/$', views.facebook_logout, name='logout'),
    url(r'^api/', include('rest_framework_swagger.urls')),
    # API Methods
    url(r'^', include(routers.router.urls)),
]
