from rest_framework.serializers import ModelSerializer
from users.models import CustomUser


class UserSerializers(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class CustomUserSerializers(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']
