from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import CustomUser, Project, TODO


class CustomUserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'projects']


class TODOHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TODO
        fields = ['text', 'project', 'created', 'author', 'is_active']


# class ShortUserModelSerializer(ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email']


class ProjectModelSerializer(ModelSerializer):
    users = CustomUser
    # users = ShortUserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'users', 'url']
