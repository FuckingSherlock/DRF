from rest_framework import generics
from users.models import CustomUser
from .serializers import CustomUserSerializers, UserSerializers


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return CustomUserSerializers
        return UserSerializers
