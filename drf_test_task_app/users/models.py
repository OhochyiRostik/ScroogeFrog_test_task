from django.db import models
from django.contrib.auth import models as auth_models

from users.manager import UserManager


class User(auth_models.AbstractUser):
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

