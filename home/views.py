from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from home.models import *
from datetime import datetime
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.all()
        for blog in blogs:
            print(blog.title)
            print(blog.description, blog.blog_image, blog.category)
        return render(request, 'home.html', {'blogs':blogs})
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
            return render(request, 'contact.html')
    else:
        messages.success(request, 'Please login first!')
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
        user_name = request.user.username
        print(user_name)
        user_id = request.user.id
        print('user id>>',user_id)
        posts = Post.objects.filter(user=user_id)
        return render(request, 'userprofile.html', {'posts':posts})
    else:
        return render(request, 'login_user.html')

def readmore(request):
    return render(request, 'readmore.html')

def addblog(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        blog__image = 'blogimages/'+ request.POST.get('blog_image')
        print(blog__image)
        blog = Blog(user=user, title=title, category=category, blog_image=blog__image, description=description)
        blog.save()
        return redirect('/')

    return render(request, 'addblog.html')

def addpost(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        post_image = 'postimages/'+str(request.POST.get('post_image'))
        post = Post(user=user, title=title, post_image=post_image)
        post.save()
        return redirect('/post')

    return render(request, 'addpost.html')

def post(request):
    posts = Post.objects.all()
    for post in posts:
        print('this is >>',post.post_image)
    return render(request, 'post.html', {'posts':posts})

def chat(request):
    return render(request, 'chat.html')