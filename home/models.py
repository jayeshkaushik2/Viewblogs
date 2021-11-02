from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=20)
    massage = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class User_profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=10000000)
    user_image = models.ImageField(upload_to='userimages', default="", null=True)
    linkedIn_url = models.CharField(max_length=10000, default="")
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    
    def total_followers(self):
        return self.followers.count()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=10000)
    post_img = models.ImageField(upload_to='postsimages')
    likes = models.ManyToManyField(User, related_name='likes')

    def total_likes(self):
        return self.likes.count()

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100000)
    category = models.CharField(max_length=1000)
    blog_img = models.ImageField(upload_to='blogimages')
    description = models.CharField(max_length=1000000)
