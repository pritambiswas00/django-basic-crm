from django.shortcuts import render, redirect
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


# //Website Main Page Renderer//
def home(request: Request) -> Response:
    # Check to see if user logged in or not
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            messages.success(request=request, message="You are currently logged in.")
            return redirect("home")
        else:
            messages.success(
                request=request, message="There was an login error. Please try again."
            )
            return redirect("home")
    else:
        return render(request, "home.html", {})


# logout user
def logout_user(request: Request) -> Response:
    logout(request=request)
    messages.success(request=request, message="You have successfully logged out.")
    return redirect("home")


# Register User
def register_user(request: Request) -> Response:
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request=request, user=user)
            messages.success(
                request=request, message="You have successfully registered."
            )
            return redirect("home")
    else:
        form = SignUpForm()
        return render(
            request=request, template_name="register.html", context={"form": form}
        )
    return render(
        request=request, template_name="register.html", context={"form": form}
    )
