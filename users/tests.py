from .models import CustomUser, Project, TODO
from .views import CustomUserViewSet

from mixer.backend.django import mixer
from rest_framework.test import APIRequestFactory, force_authenticate,  APIClient, APISimpleTestCase, APITestCase
from urllib import response
from django.test import TestCase
from rest_framework import status

DJANGO_SETTINGS_MODULE = 'config/settings'


# from django.contrib.auth.models import User


class TestUserViewSet(TestCase):

    def setUp(self):
        self.url = '/api/users/'
        self.users = {
            "id": 2,
            "username": "FuckingSherlock",
            "first_name": "Sherlock",
            "last_name": "Fucking",
            "email": "shutn@bk.com",
            "projects": [6, 7]}
        self.users_fake = {
            "id": 1,
            "username": "Fucklock",
            "first_name": "Sk",
            "last_name": "Fg",
            "email": "sh@bk.cm",
            "projects": [0]}
        self.format = 'json'
        self.login = 'admin'
        self.password = 'admin'
        self.admin = CustomUser.objects.create_superuser(self.login, 'admin@mail.ru', self.password)
        self.user = CustomUser.objects.create(**self.users)

    def test_factory_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = CustomUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_factory_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.users, format=self.format)
        view = CustomUserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_factory_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.users, format=self.format)
        force_authenticate(request, self.admin)
        view = CustomUserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_client_detail(self):
        client = APIClient
        response = client.get(f'{self.url}{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_client_update_guest(self):
        client = APIClient
        response = client.put(f'{self.url}{self.user.id}/', **self.users_fake)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_client_create_admin(self):
        client = APIClient
        client.login(self.admin)
        response = client.put(f'{self.url}{self.user.id}/', **self.users_fake, format=self.format)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.users.refresh_from_db()
        self.assertEqual(self.users.id, self.users_fake.get('id'))
        self.assertEqual(self.users.username, self.users_fake.get('username'))
        self.assertEqual(self.users.first_name, self.users_fake.get('first_name'))
        self.assertEqual(self.users.last_name, self.users_fake.get('last_name'))
        self.assertEqual(self.users.email, self.users_fake.get('email'))
        self.assertEqual(self.users.projects, self.users_fake.get('projects'))

        client.logout()

    def tearDown(self):
        pass


class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        import math
        response = math.sqrt(4)
        self.assertEqual(response, 2)


class TestProject(APITestCase):

    def setUp(self):
        self.users_dict = {'id': 1, "username": "FuckingSherlock", "first_name": "Sherlock",
                           "last_name": "Fucking", "email": "shutn@bk.com"}
        self.url = '/api/todos/'
        self.format = 'json'
        self.login = 'admin'
        self.password = 'admin'
        self.admin = CustomUser.objects.create_superuser(self.login, 'admin@mail.ru', self.password)
        # self.users = CustomUser.objects.create(**self.users_dict)
        self.users = CustomUser.objects.create(**self.users_dict)
        print(self.users)
        self.projects_dict = {'url': 'urllll', 'id': 1, 'name': 'any', 'users': self.users}
        self.projects = Project.objects.create(**self.projects_dict)
        self.todo = {'text': 'some TODO', 'project': self.projects, 'author': self.admin}
        self.todos = TODO.objects.create(**self.projects_dict)

    def test_api_test_case_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_api_test_case_update_admin(self):

        # def test_api_

    def tearDown(self):
        pass
