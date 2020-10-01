from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.index, name="indexPage"),
    path('add-post', views.add_post, name="new-post"),
    path('about', views.about, name="about-page"),
    path('contact', views.contact, name="contact-page"),
    path('create', views.create),
    path('full-post/<int:post_id>', views.full_post),
    path('login-iblog', views.login_iblog),
    path('delete-post/<int:post_id>', views.delete_post),
    path('update-post/<int:post_id>', views.update_post),
    path('member-data', views.member_data),
    path('logout', views.logoutUser),
    path('update/<int:post_id>', views.Update),
    path('login', views.loginUser),
]