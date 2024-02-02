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


class EditBorrowedBookForm(ModelForm):
    class Meta:
        model = BorrowedBook
        fields = [
            "borrowed_date",
            "returned_date",
            "fine",
        ]
