from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
# сравнил варианты choice полей из документации, 
# с использованием класса для меня показалась самой короткой и простой
    class UserRole(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    role = models.CharField(
        max_length=30,
        choices=UserRole.choices,
        default=UserRole.USER,
    )
    bio = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    REQUIRED_FIELDS = ['email', 'role']

    def __str__(self):
        return self.username
