from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import Employee, Student

def index(request):
    return render(request, 'library/index.html')

def aboutus(request):
    return render(request, 'library/aboutus.html')

def services(request):
    return render(request, 'library/services.html')

def forgetpw(request):
    return render(request, 'library/forgetpw.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_mode = form.cleaned_data['user_mode']

            if user_mode == 'employee':
                # Register the user as an employee
                employee = Employee(username=username, email=email, password=password)
                employee.save()
            elif user_mode == 'student':
                # Register the user as a student
                student = Student(username=username, email=email, password=password)
                student.save()
            
            return redirect('library-login')
    else:
        form = SignupForm()

    return render(request, 'library/signup.html', {'form': form})

def user_login(request):
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
                # Check the class of the user
                if hasattr(user, 'employee'):
                    print("User is an employee")
                    return redirect('library-services')  
                elif hasattr(user, 'student'):
                    print("User is a student")
                    return redirect('library-aboutus')  
            else:
                print("Authentication failed")
                form.add_error(None, 'Invalid username or password.')  # Add a non-field error message
    else:
        form = LoginForm()

    return render(request, 'library/login.html', {'form': form})
