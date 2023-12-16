from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from image_optimizer.fields import OptimizedImageField
import uuid

class User(AbstractUser):

    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    image = OptimizedImageField(upload_to='images/users', null=True, blank=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.email


