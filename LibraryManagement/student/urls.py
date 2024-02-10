
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('request/', views.student_requestform, name='student_request'),
    path('borrowedbook/', views.student_borrowed, name='student-borrowed'),
    path('addbook/', views.addbook, name='student-addbook'),
    path('bookselves/', views.bookselves, name='student-bookselves'),
    path('deletebook/', views.deletebook, name='student-deletebook'),
    path('detailbook/<book_id>', views.detail, name='student-detailbook'),
    path('reviewbook/<book_id>', views.write_review, name='student-reviewbook'),
]

