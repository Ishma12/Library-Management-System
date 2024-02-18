from library.models import User  
from django.db import models
from django.conf import settings  
from django.utils import timezone

class MyBook(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    about=models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.book_name



