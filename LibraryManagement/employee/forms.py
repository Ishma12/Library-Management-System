from django.forms import ModelForm
from .models import Book, BorrowedBook


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
    class Meta:
        model = BorrowedBook
        fields = [
            "book",
            "student",
            "borrowed_date",
            "returned_date",
            "fine",
            "is_borrowed",
        ]

class EditBorrowedBookForm(ModelForm):
    class Meta:
        model = BorrowedBook
        fields = [
            "borrowed_date",
            "returned_date",
            "fine",
        ]
