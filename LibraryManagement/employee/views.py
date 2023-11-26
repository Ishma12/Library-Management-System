from django.shortcuts import render, redirect
from .models import Book
from .models import BorrowedBook
from django.http import JsonResponse
from datetime import datetime  
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt  # Add this import
from django.contrib.auth.decorators import login_required


@login_required
def employee(request):
    books = Book.objects.all()
     # Fetch the count of books and borrowed books
    book_count = Book.objects.count()
    borrowed_book_count = BorrowedBook.objects.count()
    return render(request, 'employee/edashboard.html', {'books': books, 'book_count': book_count, 'borrowed_book_count': borrowed_book_count})

@login_required
def book(request):
    books = Book.objects.all()
    borrowed_books = BorrowedBook.objects.all()
    book_count = Book.objects.count()
    borrowed_book_count = BorrowedBook.objects.count()
    return render(request, 'employee/ebook.html', {'books': books,'book_count': book_count,  'borrowed_books': borrowed_books,'borrowed_book_count': borrowed_book_count})

@login_required
def borrowedbook(request):
    borrowed_books = BorrowedBook.objects.all()
    book_count = Book.objects.count()
    borrowed_book_count = BorrowedBook.objects.count()
    return render(request, 'employee/eborrowedbook.html', {'book_count': book_count,  'borrowed_books': borrowed_books,'borrowed_book_count': borrowed_book_count})


def changepw(request):
    return render(request, 'employee/changepw.html')

@login_required
def addbook(request):
    if request.method == 'POST':
        # Process the form data and save the book
        book_id = request.POST.get('bookID')
        book_name = request.POST.get('bookName')
        author = request.POST.get('author')
        category = request.POST.get('category')
        price = request.POST.get('price')


        # Save the book to the database
        book = Book.objects.create(
            book_id=book_id,
            book_name=book_name,
            author=author,
            category=category,
            price=price
        )

        # Return the added book details as JSON response
        return JsonResponse({
            'book_id': book.book_id,
            'book_name': book.book_name,
            'author': book.author,
            'category': book.category,
            'price': str(book.price)  
        })


    return render(request, 'employee/addbook.html')

@login_required
def editbook(request):
    if request.method == 'POST':
        book_id = request.POST.get('bookID')
        new_book_name = request.POST.get('bookName')
        new_author = request.POST.get('author')
        new_category = request.POST.get('category')
        new_price = request.POST.get('price')

        # Use filter to handle multiple books with the same ID
        books = Book.objects.filter(book_id=book_id)

        if books.exists():
            # Iterate over the queryset and update each book
            for book in books:
                book.book_name = new_book_name
                book.author = new_author
                book.category = new_category
                book.price = new_price
                book.save()

            # Return a success message as JSON response
            return JsonResponse({'message': 'Books updated successfully'})
        else:
            # Return an error message as JSON response if no books are found
            return JsonResponse({'error': 'No books found for the specified ID'}, status=400)

    # If the request method is not POST, render the editbook.html template
    return render(request, 'employee/editbook.html')


@login_required
def deletebook(request):
    if request.method == 'POST':
        book_id = request.POST.get('bookID')

        # Use filter instead of get to handle multiple books with the same ID
        books = Book.objects.filter(book_id=book_id)

        if books.exists():
            # Iterate over the queryset and delete each book
            for book in books:
                book.delete()

            # Return a success message as JSON response
            return JsonResponse({'message': 'Books deleted successfully'})
        else:
            # Return an error message as JSON response if no books are found
            return JsonResponse({'error': 'No books found for the specified ID'}, status=400)

    # If the request method is not POST, render the deletebook.html template
    return render(request, 'employee/deletebook.html')




@login_required
def addborrowedbook(request):
    if request.method == 'POST':
        # Process the form data and save the borrowed book
        borrowedbook_id = request.POST.get('borrowedbookID')
        borrowedbook_name = request.POST.get('borrowedbookName')
        student_id = request.POST.get('studentID')
        student_name = request.POST.get('studentName')
        borrowed_date = request.POST.get('borrowdate')
        returned_date = request.POST.get('returndate')
        fine=request.POST.get('fine')

        # Save the borrowed book to the database
        borrowed_book = BorrowedBook.objects.create(
            borrowedbook_id=borrowedbook_id,
            borrowedbook_name=borrowedbook_name,
            student_id=student_id,
            student_name=student_name,
            borrowed_date=borrowed_date,
            returned_date=returned_date,
            fine=fine
        )

        # Return the added borrowed book details as JSON response
        return JsonResponse({
            'borrowedbook_id': borrowed_book.borrowedbook_id,
            'borrowedbook_name': borrowed_book.borrowedbook_name,
            'student_id': borrowed_book.student_id,
            'student_name': borrowed_book.student_name,
            'borrowed_date': str(borrowed_book.borrowed_date),
            'returned_date': str(borrowed_book.returned_date) if borrowed_book.returned_date else None,
            'fine': str(borrowed_book.fine)
        })


    return render(request, 'employee/addborrowedbook.html')



@login_required
def editborrowedbook(request):
    if request.method == 'POST':
        borrowedbook_id = request.POST.get('borrowedbookID')
        new_borrowedbook_name = request.POST.get('borrowedbookName')
        new_student_id = request.POST.get('studentID')
        new_student_name = request.POST.get('studentName')
        new_borrowed_date = request.POST.get('borrowdate')
        new_returned_date = request.POST.get('returndate')
        new_fine = request.POST.get('fine')

        # Use filter to handle multiple borrowed books with the same ID
        borrowed_books = BorrowedBook.objects.filter(borrowedbook_id=borrowedbook_id)

        if borrowed_books.exists():
            # Iterate over the queryset and update each borrowed book
            for borrowed_book in borrowed_books:
                borrowed_book.borrowedbook_name = new_borrowedbook_name
                borrowed_book.student_id = new_student_id
                borrowed_book.student_name = new_student_name
                borrowed_book.borrowed_date = new_borrowed_date
                borrowed_book.returned_date = new_returned_date
                borrowed_book.fine = new_fine
                borrowed_book.save()

            # Return a success message as JSON response
            return JsonResponse({'message': 'Borrowed books updated successfully'})
        else:
            # Return an error message as JSON response if no borrowed books are found
            return JsonResponse({'error': 'No borrowed books found for the specified ID'}, status=400)

    # If the request method is not POST, render the editborrowedbook.html template
    return render(request, 'employee/editborrowedbook.html')

@login_required
def deleteborrowedbook(request):
    if request.method == 'POST':
        borrowedbook_id = request.POST.get('borrowedbookID')

        # Use filter instead of get to handle multiple borrowed books with the same ID
        borrowed_books = BorrowedBook.objects.filter(borrowedbook_id=borrowedbook_id)

        if borrowed_books.exists():
            # Iterate over the queryset and delete each borrowed book
            for borrowed_book in borrowed_books:
                borrowed_book.delete()

            # Return a success message as JSON response
            return JsonResponse({'message': 'Borrowed books deleted successfully'})
        else:
            # Return an error message as JSON response if no borrowed books are found
            return JsonResponse({'error': 'No borrowed books found for the specified ID'}, status=400)

    # If the request method is not POST, render the deleteborrowedbook.html template
    return render(request, 'employee/deleteborrowedbook.html')



