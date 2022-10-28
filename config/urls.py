from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewSet,  TODOModelViewSet, ProjectDjangoFilterViewSet
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()
router.register('users', CustomUserViewSet)
router.register('projects', ProjectDjangoFilterViewSet)
router.register('todo', TODOModelViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Workspace",
        default_version='v1',
        description="Development platform",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@mail.ru"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path(r'^swagger(?P\.json|\.yaml)$', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('', include('userapp.urls')),
    # path('api/users/v1', include('userapp.urls', namespace='v1')),
    # path('api/users/v2', include('userapp.urls', namespace='v2')),
]
