from django.urls import path, include
from .views import UserModelViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('', UserModelViewSet)
print(router.urls)
app_name = 'EMSUser'
urlpatterns = [

] + router.urls
