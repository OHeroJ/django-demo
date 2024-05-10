from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # null 与数据库相关，blank 与验证相关
    age = models.PositiveIntegerField(null=True, blank=True)
