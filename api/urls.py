from .views import *
from django.conf.urls import url 
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', TaskViewSet)

urlpatterns = [
	path('task/', include(router.urls)),
]
