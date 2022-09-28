from .serializers import CustomUserModelSerializer, ProjectModelSerializer, TODOHyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser, Project, TODO


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOHyperlinkedModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
