from django.shortcuts import render, redirect
from .models import Contact, BlogPost
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def index(request):
    blog_posts = BlogPost.objects.all().order_by("-added_date")
    return render(request, "index.html", {
        "blog_posts": blog_posts
    })
    

def create(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, "create-post.html")

def add_post(request):
    blog_title = request.POST.get("blog-title")
    blog_content = request.POST.get("blog-content")
    blog_author = request.POST.get("blog-author")
    new_post = BlogPost(title=blog_title, content=blog_content, author=blog_author, added_date=timezone.now())
    new_post.save()
    return redirect("/")
def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        client_name = request.POST.get("user-name")
        client_phone = request.POST.get("user-phone")
        client_email = request.POST.get("user-email")
        client_desc = request.POST.get("user-message")
        user_contact = Contact(name=client_name, phone=client_phone, email=client_email, message=client_desc, date_time=timezone.now())
        user_contact.save()
        messages.success(request, 'Your Contact has been sent!!')
    return render(request, "contact.html")


def full_post(request, post_id):
    f_post = BlogPost.objects.get(id=post_id)
    
    return render(request, "fullpost.html", {
         "f_post": f_post
    })


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/create")
        else:
            return redirect("/")
    return redirect("/")



def login_iblog(request):
    return render(request, "login.html")


def member_data(request):
    posts = BlogPost.objects.all().order_by("-added_date")
    if request.user.is_anonymous:
        return redirect("/create")
    return render(request, "member.html", {
                "posts": posts
            })

def delete_post(request, post_id):
    post = BlogPost.objects.get(id = post_id).delete()
    return redirect("/member-data")

def update_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, "update-post.html", {
        "post": post
    })
def Update(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    if request.method == "POST":
        title = request.POST.get("blog-title")
        content = request.POST.get("blog-content")
        author = request.POST.get("blog-author")
        post.title = title
        post.content = content
        post.author = author
        post.save()
        return redirect("/member-data")
def logoutUser(request):
    logout(request)
    return redirect("/")
    
# python manage.py runserver
# python manage.py migrate
# python manage.py makemigrations