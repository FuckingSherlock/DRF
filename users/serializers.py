from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import CustomUser, Project, TODO
from django.contrib.auth.hashers import make_password


class CustomUserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'projects']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(self, CustomUserModelSerializer).create(validated_data)


class ProjectModelSerializer(ModelSerializer):
    users = CustomUser

    class Meta:
        model = Project
        fields = ['id', 'name', 'users', 'url', 'todo']


class TODOHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    project = ProjectModelSerializer()

    class Meta:
        model = TODO
        fields = ['id', 'text', 'project', 'created', 'author', 'is_active']
