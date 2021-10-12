from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('signup', views.signup, name='signup'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('readmore', views.readmore, name='readmore'),
    path('addblog', views.addblog, name='addblog'),
    path('addpost', views.addpost, name='addpost'),
    path('post', views.post, name='post'),
    path('like_pressed', views.like_pressed, name='like_pressed'),
    path('chat', views.chat, name='chat'),
    path('editprofile', views.editprofile, name='editprofile'),
]