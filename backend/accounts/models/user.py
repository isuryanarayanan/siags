from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


"""
User modes decide which permissions each user will recieve
"""
user_modes = (
    (1, 'student'),
    (2, 'teacher'),
    (3, 'administrator')
)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, mode, password, **extra_fields):
        """
        Create and save a user with the given username, email, mode, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email,
                          mode=mode, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, mode=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, mode, password, **extra_fields)

    def create_superuser(self, username, email=None, mode=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, mode, password, **extra_fields)


class User(AbstractUser):

    email = models.EmailField(unique=True)
    mode = models.IntegerField(choices=user_modes, default=1, null=True)

    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        app_label = "accounts"
