
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book
from django.http import HttpResponse
from django.http import JsonResponse


def student_dashboard(request):
    return render(request, 'student/sdashboard.html')
def student_requestform(request):
    return render(request,'student/requestform.html')

def reviews(request):
    return render(request,'student/reviews.html')
def available(request):
    return render(request,'student/availablebook.html')
def borrowed(request):
    return render(request,'student/borrowedbook.html')
@login_required
def addbook(request):
    if request.method == 'POST':
        # Process the form data and save the book
        book_name = request.POST.get('bookName')
        author = request.POST.get('author')
        category = request.POST.get('category')
        about = request.POST.get('about')

        # Save the book to the database
        book = Book.objects.create(
            book_name=book_name,
            author=author,
            category=category,
            about=about,
        )

        # Return the added book details as JSON response
        return JsonResponse({
            'status': 'success',
            'book_name': book.book_name,
            'author': book.author,
            'category': book.category,
            'about': book.about,
        })

    return render(request, 'student/addbook.html')

def bookselves(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'student/bookselves.html', {'books': books})

def deletebook(request):
    if request.method == 'POST':
        book_name= request.POST.get('bookName')

        # Use filter instead of get to handle multiple books with the same ID
        books = Book.objects.filter(book_name=book_name)

        if books.exists():
            # Iterate over the queryset and delete each book
            for book in books:
                book.delete()

            # Return a success message as JSON response
            return JsonResponse({'message': 'Books deleted successfully'})
        else:
            # Return an error message as JSON response if no books are found
            return JsonResponse({'error': 'No books found for the specified name'}, status=400)

    # If the request method is not POST, render the deletebook.html template
    return render(request, 'student/deletebook.html')
