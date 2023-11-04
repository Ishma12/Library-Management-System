from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='library-index'),
    path('aboutus/',views.aboutus, name='library-aboutus'),
    path('services/',views.services, name='library-services'),
    path('signup/',views.signup, name='library-signup'),
    path('login/',views.login, name='library-login'),
    path('forgetpw/',views.forgetpw, name='library-forgetpw'),
]




    
