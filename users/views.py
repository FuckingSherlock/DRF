from .serializers import CustomUserModelSerializer, ProjectModelSerializer, TODOHyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin,  UpdateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter
from .models import CustomUser, Project, TODO


class CustomUserViewSet(ListModelMixin,
                        UpdateModelMixin,
                        GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


# class CustomUserModelViewSet(ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserModelSerializer

class TODOModelViewSet(ModelViewSet, LimitOffsetPagination):
    queryset = TODO.objects.filter(is_active=True)
    serializer_class = TODOHyperlinkedModelSerializer
    filterset_fields = ['project']
    limit = LimitOffsetPagination
    limit.default_limit = 20
    pagination_class = limit

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_active = False
        todo.save()


class ProjectDjangoFilterViewSet(ModelViewSet, LimitOffsetPagination):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    limit = LimitOffsetPagination
    limit.default_limit = 10
    pagination_class = limit
