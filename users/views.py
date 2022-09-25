
from .serializers import CustomUserModelSerializer
from rest_framework.viewsets import ModelViewSet

from .models import CustomUser


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
