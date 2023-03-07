from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Books, Post


# Create your views here.
def index(request):
    return render(request, "index.html")


def blogs(request):
    posts = Post.objects.all()
    return render(request, "blogs.html", {"posts": posts})


def bookstore(request):
    books = Books.objects.all()
    return render(request, "bookstore.html", {"books": books})


def library(request):
    books = Books.objects.all()
    return render(request, "library.html", {"books": books})


def helps(request):
    return render(request, "help.html")


def events(request):
    return render(request, "events.html")


def register(request, **extra_fields):
    if request.method == "POST":
        firstname = request.POST["Firstname"]
        lastname = request.POST["Lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["repeat password"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already exists")
                return redirect("admin-signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already in use")
                return redirect("admin-signup")
            else:
                extra_fields = {**extra_fields, "first_name": firstname, "last_name": lastname}
                user = User.objects.create_user(username=username, email=email, password=password, **extra_fields)
                user.save();
                return redirect("admin-login")
        else:
            messages.info(request, "Password not the same")
            return redirect("admin-signup")
    else:
        return render(request, "sign-up-admin.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("admin-page")
        else:
            messages.info(request, "Invalid username or password")
            return redirect("admin-login")
    else:
        return render(request, "login-admin.html")


def adminpage(request):
    return render(request, "admin-page.html")


def logout_user(request):
    auth.logout(request)
    return redirect("admin-login")


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, "posts.html", {"posts": posts})
