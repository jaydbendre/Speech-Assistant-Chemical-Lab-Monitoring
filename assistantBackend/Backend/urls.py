from django.urls import path,include
from . import views
from rest_framework import routers
from . import db_api as view_set

router = routers.DefaultRouter()

router.register("role",view_set.RoleViewSet)
router.register("department",view_set.DepartmentViewSet)
router.register("lab",view_set.LabViewSet)
router.register("user",view_set.UserViewSet)
router.register("request",view_set.RequestViewSet)
router.register("notification",view_set.NotificationViewSet)
router.register("sensor_log",view_set.Sensor_logViewSet)

urlpatterns = [
    path('', include(router.urls))
]