from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='library-index'),
    path('aboutus/', views.aboutus, name='library-aboutus'),
    path('services/', views.services, name='library-services'),
    path('login/', views.user_login, name='login'),
    path('forgetpw/', views.forgetpw, name='library-forgetpw'),
    path('signup/', views.signup, name='library-signup'),
    path('logout/',views.logoutview, name='library-logout'),
    path('verify/<username>/',views.verify_user, name='library-verify'),
    

]
