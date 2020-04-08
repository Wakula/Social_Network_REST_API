from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    last_activity = models.DateField(null=True)

    objects = BaseUserManager()

    USERNAME_FIELD = 'email'

    def update_last_activity(self):
        self.last_activity = timezone.now()
        self.save()

    def update_last_login(self):
        self.last_login = timezone.now()
        self.save()

    def __str__(self):
        return self.email
