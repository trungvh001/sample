
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from . import enums

# Create your models here.



class CustomUserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_('The username must be set'))
        username = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=255)
    role = models.CharField(choices=enums.role_choices, max_length=3, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    location = models.CharField(max_length=1000, null=True, blank=True)
    create_by = models.ForeignKey("self",
                                  on_delete=models.CASCADE,
                                  default=None,
                                  null=True,
                                  blank=True
                                  )
    createdate = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


class Truong(models.Model):
    name = models.CharField(max_length=255)
    time_start = models.DateField(null=True)
    max_person = models.IntegerField(
        validators=[
            MaxValueValidator(1000)
        ])
    location = models.CharField(max_length=255)
    create_by = models.ForeignKey(CustomUser,
                                  on_delete=models.CASCADE,
                                  default=1,
                                  null=True,
                                  blank=True
                                  )

class Khoa(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(choices=enums.department_choices, max_length=3, null=True, blank=True)
    max_person = models.IntegerField(null=True, blank=True)
    create_by = models.ForeignKey(CustomUser,
                                  on_delete=models.CASCADE,
                                  default=None,
                                  null=True,
                                  blank=True
                                  )
    createdate = models.DateTimeField(default=timezone.now)

class Lop(models.Model):
    name = models.CharField(max_length=255)
    max_person = models.IntegerField(null=True, blank=True)
    create_by = models.ForeignKey(CustomUser,
                                  on_delete=models.CASCADE,
                                  default=None,
                                  null=True,
                                  blank=True
                                  )
    createdate = models.DateTimeField(default=timezone.now)