from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField (uniqe = True)
    is_staff = models.BooleanField = False
    is_active = models.BooleanField = True
    date_joined = models.DateField(timezone.now)