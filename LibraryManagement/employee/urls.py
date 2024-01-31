from django.urls import path
from . import views
from .views import book
from .views import GeneratePDFReportView
from .views import generate_borrowed_books_excel

urlpatterns = [
    path('edashboard/', views.employee, name='employee-edashboard'),
    path('ebook/', views.book, name='employee-ebook'),
    path('eborrowedbook/', views.borrowedbook, name='employee-eborrowedbook'),
    path('changepw/', views.changepw, name='employee-changepw'),
    path('addbook/', views.addbook, name='employee-addbook'),
    path('editbook/<book_id>', views.editbook, name='employee-editbook'),
    path('deletebook/<book_id>', views.deletebook, name='employee-deletebook'),
    path('addborrowedbook/', views.addborrowedbook, name='employee-addborrowedbook'),
    path('editborrowedbook/', views.editborrowedbook, name='employee-editborrowedbook'),
    path('deleteborrowedbook/', views.deleteborrowedbook, name='employee-deleteborrowedbook'),
    path('generate_pdf_report/', GeneratePDFReportView.as_view(), name='generate_pdf_report'),
    path('generate-borrowed-books-excel/', generate_borrowed_books_excel, name='generate_borrowed_books_excel'),
    path('requestfromstudent/', views.bookrequest, name='employee-requestfromstudent'),
    path('requestfromstudent/approve/<book_id>', views.approve_bookrequest, name='employee-requestfromstudent-approve'),
    path('requestfromstudent/decline/<book_id>', views.decline_bookrequest, name='employee-requestfromstudent-decline'),
    path('book-detail/<book_id>', views.detail, name='book-detail'),

]
