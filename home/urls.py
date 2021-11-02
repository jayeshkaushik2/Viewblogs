from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # home page and contact us
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),

    # login logout and signup
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('signup', views.signup, name='signup'),
    
    # user profile, edit profile, user posts and user blogs
    path('addblog', views.addblog, name='addblog'),
    path('addpost', views.addpost, name='addpost'),
    path('post', views.post, name='post'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('editprofile', views.editprofile, name='editprofile'),
    
    # readmore blog and delete blog
    path('readmore', views.readmore, name='readmore'),
    path('deleteblog', views.deleteblog, name='deleteblog'),
    
    # post likes, shares, comments and sendto
    path('like_pressed', views.like_pressed, name='like_pressed'),

    # messages or chats
    path('chat', views.chat, name='chat'),

    # user ids from this link
    path('user', views.user, name='user'),
]