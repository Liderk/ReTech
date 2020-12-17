from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, signin, signout

router = DefaultRouter()

router.register(r'task', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('signin/', csrf_exempt(signin)),
    path('signout/', signout)
]
