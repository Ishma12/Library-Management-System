
from django.shortcuts import render,get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from employee.models import Book, Review
from employee.models import BorrowedBook
from django.http import HttpResponse
from django.http import JsonResponse
from .models import MyBook


@login_required
def student_dashboard(request):
    book_data = Book.get_book_data()
    return render(request, 'student/sdashboard.html', book_data)

@login_required
def detail(request,book_id):
    borrowed=request.GET.get('borrowed')
    msg=request.GET.get('msg')
    book= get_object_or_404(Book,id=book_id)
    return render(request, 'student/sdetail.html', {"book":book, 'borrowed': borrowed, 'msg':msg})

# def detail(request):
#     book_data = Book.get_book_data()
#     return render(request, 'student/sdetail.html', book_data)


@login_required
def student_requestform(request):
    return render(request,'student/requestform.html')

@login_required
def student_borrowed(request):
    borrowedbooks=BorrowedBook.objects.filter(student=request.user)
    return render(request,'student/borrowedbook.html', {'bbooks':borrowedbooks})

@login_required
def addbook(request):
    if request.method == 'POST':
        try:
            # Process the form data and save the book
            book_name = request.POST.get('bookName')
            author = request.POST.get('author')
            category = request.POST.get('category')
            about = request.POST.get('about')

            # Save the book to the database
            mybook = MyBook.objects.create(
                book_name=book_name,
                author=author,
                category=category,
                about=about,
                user=request.user,
            )

            # Return the added book details as JSON response
            return JsonResponse({
                'status': 'success',
                'book_name': mybook.book_name,
                'author': mybook.author,
                'category': mybook.category,
                'about': mybook.about,
            })
        except Exception as e:
            # Log the error for debugging
            print(f"Error adding book: {e}")
            # Return an error response
            return JsonResponse({'status': 'error', 'message': 'Failed to add book'}, status=500)

    return render(request, 'student/addbook.html')

@login_required
def bookselves(request):
    books = MyBook.objects.filter(user=request.user)  
    return render(request, 'student/bookselves.html', {'books': books})


@login_required
def deletebook(request):
    if request.method == 'POST':
        book_name= request.POST.get('bookName')

        # Use filter instead of get to handle multiple books with the same ID
        books = MyBook.objects.filter(book_name=book_name)

        if books.exists():
            # Iterate over the queryset and delete each book
            for mybook in books:
                mybook.delete()

            # Return a success message as JSON response
            return JsonResponse({'message': 'Books deleted successfully'})
        else:
            # Return an error message as JSON response if no books are found
            return JsonResponse({'error': 'No books found for the specified name'}, status=400)

    # If the request method is not POST, render the deletebook.html template
    return render(request, 'student/deletebook.html')


@login_required
def write_review(request, book_id):
    if request.method == "POST":
        book= get_object_or_404(Book,id=book_id)
        review =request.POST.get('review')
        rating = request.POST.get('rating')
        Review.objects.create(review=review,rating=rating, user=request.user, book=book)
    return redirect (reverse('student-detailbook',kwargs={"book_id":book_id}))
