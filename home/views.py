from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import *
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        blogs = list(Blog.objects.all())[::-1]
        user_profile = User_profile.objects.filter(user=request.user)[0]
        return render(request, 'home.html', {'blogs':blogs, 'user_profile':user_profile})
    else:
        return render(request, 'login_user.html')

def contact(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            massage = request.POST.get('massage')
            contact = Contact(name=name, email=email, password=password, massage=massage, date=datetime.today())
            contact.save()
            messages.success(request, 'Message has been sent!')
            return redirect('/')
        else:
            user_profile = User_profile.objects.filter(user=request.user)[0]
            return render(request, 'contact.html', {'user_profile':user_profile})
    else:
        user_profile = User_profile.objects.filter(user=request.user)[0]
        messages.success(request, 'Please login first!', {'user_profile':user_profile})
        return redirect('/login_user')

def login_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')
        user = authenticate(username=user_name, password=user_password)
        if user is not None:
            login_is = True
            context = {
                'login_is':login_is
            }
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, 'Your Password or Username is wrong!')

    if request.user.is_authenticated:
        messages.success(request, 'Your are already logged in!')
        return redirect('/')
    else:
        return render(request, 'login_user.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname  = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conform_password = request.POST.get('conform_password')

        if len(password) < 8:
            messages.success(request, 'Your password should be atleast of 8 characters!')
            return redirect('/signup')

        elif  password != conform_password:
            messages.success(request, 'Conform password is not matching!')
            return redirect('/signup')

        elif len(username) >= 20:
            messages.success(request, 'Your username should contain less than 20 characters!')
            return redirect('/signup')

        else:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, 
             email=email, password=password)
            user.save()
            user_profile = User_profile(user=user)
            user_profile.save()
            
            login(request, user)
            return redirect('/')

    if request.user.is_authenticated:
        messages.success(request, 'you are already logged in!')
        return redirect('/')
    else:
        return render(request, 'signup.html')

def logout_user(request):
    login_is = False
    context = {
        'login_is':login_is
    }
    logout(request)
    return render(request, 'login_user.html', context)

def userprofile(request):
    if request.user.is_authenticated:
        # username, about, followers, following, linkedurl, blogs uploaded by user, and posts uploaded by user
        user_id = request.user.id
        user_profile = User_profile.objects.filter(user=user_id)[0]
        print('user image',user_profile.user_image, user_profile)
        # posts uploaded by this user will come from this model
        posts = list(Post.objects.filter(user=user_id))[::-1]
        # about, userimages, followers will come from this model
        user_blogs = list(Blog.objects.filter(user=user_id))[::-1]
        return render(request, 'userprofile.html', {'posts':posts, 'user_profile':user_profile, 'blogs':user_blogs, 'user':request.user})
    else:
        return redirect('/login_user')

def readmore(request):
    user_profile = User_profile.objects.filter(user=request.user)[0]
    return render(request, 'readmore.html', {'user_profile':user_profile})

def addblog(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        blog__image = request.FILES['blog_image']
        print(blog__image)
        blog = Blog(user=user, title=title, category=category, blog_img=blog__image, description=description)
        blog.save()
        return redirect('/')
    user_profile = User_profile.objects.filter(user=request.user)[0]
    return render(request, 'addblog.html', {'user_profile':user_profile})

def addpost(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        post_image = request.FILES['post_image']
        print(post_image)
        post = Post(user=user, title=title, post_img=post_image)
        post.save()
        return redirect('/post')
    user_profile = User_profile.objects.filter(user=request.user)[0]
    return render(request, 'addpost.html', {'user_profile':user_profile})

def like_pressed(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    print('btn pressed liked!', post)
    return HttpResponseRedirect(reverse('post'))

def post(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user_profile = User_profile.objects.filter(user=request.user)[0]
        return render(request, 'post.html', {'posts':list(posts)[::-1], 'user_profile':user_profile})
    return redirect('/login_user')

def chat(request):
    user_profile = User_profile.objects.filter(user=request.user)[0]
    return render(request, 'chat.html', {'user_profile':user_profile})

def editprofile(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        print(user.id)
        user_profile = User_profile.objects.get(id=user.id)
        print(user_profile)
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        linkedIn_url = request.POST.get('linkedIn_url')
        about = request.POST.get('about')

        # for email and username edit 
        if user_name != str(request.user.username) or email != str(request.user.email):
            user.username = user_name
            user.email = email
            user.save()

        # for profileimage, linkedIn url and about edit
        if 'profile_img' in request.FILES:
            print('image in files...')
            user_profile.user_image = request.FILES['profile_img']

        if user_profile.linkedIn_url != linkedIn_url:
            user_profile.linkedIn_url = linkedIn_url
        
        user_profile.about = about
        user_profile.save()

        print('saved!')
        return redirect('/editprofile')

    user_profile = User_profile.objects.filter(user=request.user.id)[0]
    return render(request, 'editprofile.html', {'user_profile':user_profile})

def deleteblog(request):
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        print(blog_id)
        return redirect('/userprofile')

def user(request):
    # if user id equals to request.user.id return to userprofile page
    path = request.get_full_path()
    user_id = int(path.split('-')[-1])
    if user_id == int(request.user.id):
        return redirect(f'/userprofile?={request.user.username}')
    else:
        user = User.objects.get(id=user_id)
        # user profile,user blogs, AND user posts
        # user profile can be empty
        user_profile = User_profile.objects.filter(user=user_id)[0]
        blogs = Blog.objects.filter(user=user_id)
        posts = Post.objects.filter(user=user_id)
        print(user, user_profile, blogs, posts)

        return render(request, 'userprofile.html', {'blogs':blogs, 'posts':post, 'user_profile':user_profile, 'user':user})
        return HttpResponse('this iss it')