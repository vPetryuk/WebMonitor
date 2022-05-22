from django.urls import path, include
from rest_framework import routers

from .views import FailuresViewSet, WebPageViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'webpage-viewset', WebPageViewSet) 
router.register(r'failure-viewset', FailuresViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]


