from urllib import request
from .serializers import CustomUserModelSerializer, ProjectModelSerializer, TODOHyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, BasePermission
from .filters import ProjectFilter
from .models import CustomUser, Project, TODO
from rest_framework.settings import api_settings


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


# class CustomUserViewSet(RetrieveModelMixin,
#                         ListModelMixin,
#                         UpdateModelMixin,
#                         GenericViewSet):
    # permission_classes = [AllowAny]
class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


class CustomLimitOffsetPagination(LimitOffsetPagination):

    def __init__(self, default_limit=api_settings.PAGE_SIZE, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_limit = default_limit


class ViewPaginatorMixin:
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                if getattr(self, 'paginate_limit', None):
                    self._paginator = self.pagination_class(
                        default_limit=getattr(self, 'paginate_limit', None))
                else:
                    self._paginator = self.pagination_class()
        return self._paginator


class TODOModelViewSet(ViewPaginatorMixin, ModelViewSet):
    queryset = TODO.objects.filter(is_active=True)
    serializer_class = TODOHyperlinkedModelSerializer
    filterset_fields = ['project']
    paginate_limit = 2
    pagination_class = CustomLimitOffsetPagination

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_active = False
        todo.save()


class ProjectDjangoFilterViewSet(ViewPaginatorMixin, ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    paginate_limit = 2
    pagination_class = CustomLimitOffsetPagination
