from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):

    username = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=64)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    is_staff = models.BooleanField(
        _("staff status"),
        default=False)

    is_superuser = models.BooleanField(
        _("staff status"),
        default=False)

    def __str__(self):
        return self.username + '\n' + self.email


class Project(models.Model):
    url = models.URLField(default='url')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    users = models.ManyToManyField(CustomUser, related_name="projects")


class TODO(models.Model):
    text = models.TextField(blank=True, null=True)
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
