from django.urls import path, include, re_path
from EMSDevice import views
from rest_framework.routers import SimpleRouter

app_name = 'EMSDevice'
router = SimpleRouter()
router.register('', views.DeviceModelViewSet)

urlpatterns = [

]+router.urls
