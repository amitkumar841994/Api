
from django.contrib import admin
from django.urls import path,include
from restapi.views import studentviewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'student',studentviewset)

urlpatterns = [
    path('',include(router.urls))

]
