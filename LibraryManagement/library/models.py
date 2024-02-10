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



class Notification(models.Model): 
    created_on = models.DateTimeField(auto_now_add=True)
    detail=models.CharField(max_length=255)
    is_read=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
