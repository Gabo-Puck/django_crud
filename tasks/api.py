from tasks.models import Task
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()#dataset to query
    permission_classes = [permissions.AllowAny] #which clients can query this resource
    serializer_class = ProjectSerializer #how is going to convert data