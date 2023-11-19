from django.shortcuts import render, redirect
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


# //Website Main Page Renderer and also login page if not authenticated//
def home(request: Request) -> Response:
    # Check to see if user logged in or not
    records = Record.objects.all()
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
        return render(request, "home.html", {"records": records})


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

#All Records
def record_user(request: Request, id: int) -> Response:
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=id)
        return render(
            request=request,
            template_name="record.html",
            context={"customer_record": customer_record},
        )
    else:
        messages.success(request, "You are not authorized to access.")
        return redirect("home")

#Delete Records
def delete_record(request: Request, id: int) -> Response:
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=id)
        if customer_record is None:
            messages.success(request, "No Record found.")
            return redirect("home")
        else:
            deleted_record = Record.objects.get(id=id)
            deleted_record.delete()
            messages.success(request, "Successfully deleted the record.")
            return redirect("home")
    else:
        messages.success(request, "You are not authorized to access.")
        return redirect("home")

#Add Records
def add_record(request:Request)->Response:
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            added_record = form.save()
            messages.success(request,"Successfully added record.")
            return redirect('home')
        else:
            return render(request,'add_record.html',{ 'form':form })
    else:
        messages.success(request,"You are not authorized to access.")
        return redirect('home')

#Update Records
def update_record(request:Request, id:int)->Response:
    if request.user.is_authenticated:
        record_details = Record.objects.get(id=id)
        form = AddRecordForm(request.POST or None, instance=record_details)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully updated.")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request,"You are not authorized to access.")
        return redirect('home')