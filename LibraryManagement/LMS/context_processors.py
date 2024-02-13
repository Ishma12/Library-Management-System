from library.models import User
from employee.models import BorrowedBook, Book 



def default_context(request):
    student_count= User.objects.filter(usertype=User.STUDENT).count()
    book_count = Book.objects.count()
    borrowed_book_count = BorrowedBook.objects.count()
    return {
        "user_fullname": request.user.username
        if request.user.is_authenticated
        else "--",
        "book_count": book_count,
        "borrowed_book_count": borrowed_book_count,
        "student_count": student_count,
    }
