from rest_framework import viewsets
from . import serializers
from . import models

class RoleViewSet(viewsets.ModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = serializers.RoleSerializer
    
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    
class LabViewSet(viewsets.ModelViewSet):
    queryset = models.Lab.objects.all()
    serializer_class = serializers.LabSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = models.Request.objects.all()
    serializer_class = serializers.RequestSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationSerializer

class Sensor_logViewSet(viewsets.ModelViewSet):
    queryset = models.Sensor_log.objects.all()
    serializer_class = serializers.Sensor_logSerializer
