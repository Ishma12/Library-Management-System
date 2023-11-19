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
    return redirect ('library-login')


def user_login(request):
    if request.user.is_authenticated:
        if request.user.usertype== User.EMPLOYEE:
            return redirect('employee-edashboard')
        elif request.user.usertype==User.STUDENT:
            return redirect('library-services')
       
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
                    return redirect('library-services')
    
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
            user_mode = form.cleaned_data['user_mode']
            user = User(username=username,email=email,password=password,usertype=user_mode)
            user.set_password(password)
            user.save()
            return redirect('library-login')
    else:
        form = SignupForm()

    return render(request, 'library/signup.html', {'form': form})
