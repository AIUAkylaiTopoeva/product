from django.urls import include, path
from rest_framework import routers
from .views import PostView

router = routers.DefaultRouter()
router.register('products', PostView)

urlpatterns = [
    path('', include(router.urls)),
]