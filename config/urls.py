from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
