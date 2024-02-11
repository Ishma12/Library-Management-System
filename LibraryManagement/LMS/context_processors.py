from employee.models import Book
from employee.models import BorrowedBook


def default_context(request):
    # return {'user_fullname': "--"}
    book_count = Book.objects.count()
    borrowed_book_count = BorrowedBook.objects.count()
    return {
        "user_fullname": request.user.username
        if request.user.is_authenticated
        else "--",
        "book_count": book_count,
        "borrowed_book_count": borrowed_book_count,
    }
