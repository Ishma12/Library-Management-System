from django.forms import ModelForm
from .models import Book, BorrowedBook
from django import forms
from django.contrib.auth import get_user_model


User=get_user_model()

# Create the form class.
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "image",
            "isbn",
            "book_name",
            "publication_date",
            "description",
            "author",
            "subject",
            "publisher",
            "edition",
            "is_available",
        ]


class EditBookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "image",
            "isbn",
            "book_name",
            "publication_date",
            "description",
            "author",
            "subject",
            "publisher",
            "edition",
            "is_available",
        ]

class AddBorrowedBookForm(ModelForm):
    student = forms.ModelChoiceField(queryset=User.objects.filter(usertype=User.STUDENT), empty_label="(Select)")

    class Meta:
        
        model = BorrowedBook
        fields = [
            "book",
            "student",
            "borrowed_date",
            "returned_date",
            
            
        ]

class EditBorrowedBookForm(ModelForm):
    class Meta:
        model = BorrowedBook
        fields = [
            "borrowed_date",
            "returned_date",
            "fine",
        ]
