import graphene
from graphene import ObjectType, Mutation
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


class CustomUserUpdateMutation(Mutation):
    class Arguments:
        username = graphene.String(required=True)
        id = graphene.ID()

    user = graphene.Field(CustomUserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = CustomUser.objects.get(id=kwargs.get('id'))
        user.username = kwargs.get('username')
        user.save()
        return cls(user=user)


class CustomUserCreateMutation(Mutation):
    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)

    user = graphene.Field(CustomUserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = CustomUser.objects.create(**kwargs)
        return cls(user=user)


class CustomUserDeleteMutation(Mutation):
    class Arguments:
        id = graphene.ID()

    users = graphene.List(CustomUserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        CustomUser.objects.get(id=kwargs.get('id')).delete()
        return cls(users=CustomUser.objects.all())


class Mutations(ObjectType):
    update_user = CustomUserUpdateMutation
    create_user = CustomUserCreateMutation
    delete_user = CustomUserDeleteMutation


class Query(ObjectType):
    all_users = graphene.List(CustomUserType)
    all_projects = graphene.List(ProjectType)
    all_todos = graphene.List(TODOType)

    user_by_id = graphene.List(CustomUserType, id=graphene.Int(required=False))

    def resolve_user_by_id(root, info, id=None):
        if id:
            return CustomUser.objects.get(id=id)
        return CustomUser.objects.all()

    project_by_user = graphene.List(ProjectType, username=graphene.String(required=False))

    def resolve_project_by_user(root, info, username=None):
        if username:
            return Project.objects.filter(users__username=username)
        return Project.objects.all()

    def resolve_all_users(root, info):
        return CustomUser.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todos(root, info):
        return TODO.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutations)
