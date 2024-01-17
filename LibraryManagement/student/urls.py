
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('request/', views.student_requestform, name='student_request'),
    path('reviews/', views.reviews, name='student-reviews'),
    path('available/', views.available, name='student-availablebook'),
    path('bookselves/', views.available, name='student-addbook'),
]
