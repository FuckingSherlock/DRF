from .serializers import AuthorModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Author


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
