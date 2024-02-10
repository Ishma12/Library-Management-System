from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy

from .forms import LoginForm, SignupForm
from .models import User, Notification


def index(request):
    return render(request, "library/index.html")


def aboutus(request):
    return render(request, "library/aboutus.html")


def services(request):
    return render(request, "library/services.html")


def forgetpw(request):
    return render(request, "library/forgetpw.html")


def logoutview(request):
    logout(request)
    return redirect("login")


def staff_or_superuser_required(
    function=None, redirect_field_name=None, unauthorized_url=reverse_lazy("login")
):
    actual_decorator = user_passes_test(
        lambda u: u.is_staff or u.is_superuser,
        login_url=unauthorized_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


@login_required
@staff_or_superuser_required
def verify_user(request, username, *args, **kwargs):
    if request.method == "GET":
        user = get_object_or_404(User, username=username)
        user.is_active = True
        current_site = get_current_site(request=request).domain
        relative_link = reverse(
            "login",
        )
        abs_url = "http://" + current_site + relative_link
        email_body = render_to_string(
            "library/user-register-email-success.html",
            {"username": user.username, "email": user.email, "login_url": abs_url},
        )
        data = {
            "email_body": email_body,
            "to_email": user.email,
            "email_subject": "Account Verified!!",
        }

        email = EmailMessage(
            subject=data["email_subject"],
            body=data["email_body"],
            to=[data["to_email"]],
        )
        email.content_subtype = "html"
        email.send()
        user.save()
        return redirect(reverse("admin:library_user_changelist"))
    redirect(reverse("admin:library_user_changelist"))


def user_login(request):
    if request.user.is_authenticated:
        if request.user.usertype == User.EMPLOYEE:
            return redirect("employee-edashboard")
        elif request.user.usertype == User.STUDENT:
            return redirect("student_dashboard")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Attempt to authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                print(f"User authenticated: {user}")
                login(request, user)
                if user.usertype == User.EMPLOYEE:
                    return redirect("employee-edashboard")
                elif user.usertype == User.STUDENT:
                    return redirect("student_dashboard")

            else:
                print("Authentication failed")
                form.add_error(
                    None, "Invalid username or password."
                )  # Add a non-field error message
    else:
        form = LoginForm()

    return render(request, "library/login.html", {"form": form})


def signup(request):
    if request.user.is_authenticated:
        if request.user.usertype == User.EMPLOYEE:
            return redirect("employee-edashboard")
        elif request.user.usertype == User.STUDENT:
            return redirect("student_dashboard")
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            usermode = form.cleaned_data["usermode"]
            user = User(
                username=username, email=email, password=password, usertype=usermode
            )
            user.set_password(password)
            user.is_active = False
            user.save()
            return redirect("login")
    else:
        form = SignupForm()

    return render(request, "library/signup.html", {"form": form})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = "library/password_reset.html"
    email_template_name = "library/password_reset_email.html"
    subject_template_name = "library/password_reset_subject.txt"
    success_message = (
        "We've emailed you instructions for setting your password, "
        "if an account exists with the email you entered. You should receive them shortly."
        " If you don't receive an email, "
        "please make sure you've entered the address you registered with, and check your spam folder."
    )
    success_url = reverse_lazy("library-index")
    # from_email="eeshmarai@gmail.com"


def notifications(request):
    nn=Notification.objects.filter(user=request.user).order_by('-created_on')
    unread_count=nn.filter(is_read=False).count()
    data = list(nn.values())
    return JsonResponse({"data":data, "unread_count":unread_count})



def mark_as_read(request):
    nn=Notification.objects.filter(user=request.user, is_read=False)
    to_update=[]
    for n in nn:
        n.is_read=True
        to_update.append(n)
    Notification.objects.bulk_update(to_update,['is_read'])
    return JsonResponse({"success":True})