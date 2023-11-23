from django.urls import path
from . import views
from .views import book

urlpatterns = [
    path('edashboard/', views.employee, name='employee-edashboard'),
    path('ebook/', views.book, name='employee-ebook'),
    path('eborrowedbook/', views.borrowedbook, name='employee-eborrowedbook'),
    path('changepw/', views.changepw, name='employee-changepw'),
    path('addbook/', views.addbook, name='employee-addbook'),
    path('editbook/', views.editbook, name='employee-editbook'),
    path('deletebook/', views.deletebook, name='employee-deletebook'),
    path('addborrowedbook/', views.addborrowedbook, name='employee-addborrowedbook'),
    path('editborrowedbook/', views.editborrowedbook, name='employee-editborrowedbook'),
    path('deleteborrowedbook/', views.deleteborrowedbook, name='employee-deleteborrowedbook'),
    
]
