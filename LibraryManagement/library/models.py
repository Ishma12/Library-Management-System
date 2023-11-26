from django.db import models
from django.contrib.auth.models import AbstractUser
    
class User(AbstractUser):
    EMPLOYEE ="employee"
    STUDENT="student"
    USERTYPE_CHOICES=[
        (EMPLOYEE,"Employee"),
        (STUDENT,"Student"),
    ]
    usertype= models.CharField(max_length=10,choices=USERTYPE_CHOICES)

    email = models.EmailField(unique=True)
