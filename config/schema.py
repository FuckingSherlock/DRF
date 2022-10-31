import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from users.models import CustomUser, Project, TODO


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TODOType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class Query(ObjectType):
    # hellow = graphene.String(default_value='Hi!')
    all_users = graphene.List(CustomUserType)
    all_projects = graphene.List(ProjectType)
    all_todos = graphene.List(TODOType)

    def resolve_all_users(root, info):
        return CustomUser.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todos(root, info):
        return TODO.objects.all()


schema = graphene.Schema(query=Query)
