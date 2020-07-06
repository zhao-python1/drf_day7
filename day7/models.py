from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phnoe = models.CharField(max_length=10,unique= True)
    class Meta:
        db_table = "day7_user"
        verbose_name="用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
