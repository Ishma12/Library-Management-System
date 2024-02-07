
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('request/', views.student_requestform, name='student_request'),
    path('reviews/', views.reviews, name='student-reviews'),
    path('addbook/', views.addbook, name='student-addbook'),
    path('bookselves/', views.bookselves, name='student-bookselves'),
    path('deletebook/', views.deletebook, name='student-deletebook'),
    path('detailbook/<book_id>', views.detail, name='student-detailbook'),
]

