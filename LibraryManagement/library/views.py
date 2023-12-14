from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from .models import User

def index(request):
    return render(request, 'library/index.html')

def aboutus(request):
    return render(request, 'library/aboutus.html')

def services(request):
    return render(request, 'library/services.html')

def forgetpw(request):
    
    return render(request, 'library/forgetpw.html')

def logoutview(request):
    logout(request)
    return redirect ('login')


def user_login(request):
    if request.user.is_authenticated:
        if request.user.usertype== User.EMPLOYEE:
            return redirect('employee-edashboard')
        elif request.user.usertype==User.STUDENT:
            return redirect('library-index')
       
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Attempt to authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                print(f"User authenticated: {user}")
                login(request, user)
                if user.usertype== User.EMPLOYEE:
                    return redirect('employee-edashboard')
                elif user.usertype==User.STUDENT:
                    return redirect('library-index')
    
            else:
                print("Authentication failed")
                form.add_error(None, 'Invalid username or password.')  # Add a non-field error message
    else:
        form = LoginForm()

    return render(request, 'library/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            usermode = form.cleaned_data['usermode']
            user = User(username=username,email=email,password=password,usertype=usermode)
            user.set_password(password)
            user.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'library/signup.html', {'form': form})
    
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'library/password_reset.html'
    email_template_name = 'library/password_reset_email.html'
    subject_template_name = 'library/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('library-index')
    # from_email="eeshmarai@gmail.com"