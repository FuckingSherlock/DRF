from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
# ,CustomUserModelViewSet, ProjectModelViewSet,
from users.views import CustomUserViewSet,  TODOModelViewSet, ProjectDjangoFilterViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()
router.register('users', CustomUserViewSet)
# router.register('users', CustomUserModelViewSet)
# router.register('projects', ProjectModelViewSet)
router.register('projects', ProjectDjangoFilterViewSet)
router.register('todo', TODOModelViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path(r'^swagger(?P\.json|\.yaml)$', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
