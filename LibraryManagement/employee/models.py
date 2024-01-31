from django.contrib.auth.models import User  
from django.db import models
from django.conf import settings  
from django.utils import timezone

class Book(models.Model):
    '''Image
    Book Name
    IBSN
    Publication Date
    Description
    Author
    Subject
    Publisher
    Edition
    Status'''
    image=models.ImageField(upload_to ='book-images/')
    isbn = models.CharField(max_length=255)
    book_name = models.CharField(max_length=255)
    publication_date=models.DateField()
    description=models.TextField()
    author = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    publisher=models.CharField(max_length=255)
    edition=models.CharField(max_length=255)
    is_available=models.BooleanField(default=True)

    
    @classmethod
    def get_book_data(cls):
        books = cls.objects.all()
        borrowed_books = BorrowedBook.objects.all()
        book_count = cls.objects.count()
        borrowed_book_count = BorrowedBook.objects.count()
        return {'books': books,'book_count': book_count,  'borrowed_books': borrowed_books,'borrowed_book_count': borrowed_book_count}

    def __str__(self):
        return self.book_name



class BorrowedBook(models.Model):
    borrowedbook_id = models.AutoField(primary_key=True)
    borrowedbook_name = models.CharField(max_length=255, null=False, blank=False)
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=255)
    borrowed_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)
    fine = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.borrowedbook_name


class BookRequest(models.Model):
    student_id = models.CharField(max_length=50)
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    is_approved=models.BooleanField(default=None, null=True, blank=True) 
    def __str__(self):
        return f'{self.student_id} - {self.book_name}'


