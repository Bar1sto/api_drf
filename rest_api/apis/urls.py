from django.urls import path, include
from rest_framework import routers
from .views import ApiViesSet

router = routers.DefaultRouter()
router.register(r'api', ApiViesSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]