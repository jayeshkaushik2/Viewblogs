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


# class User_profile(models.Model):
#     user = models.OneToOneField(User)
#     about = models.CharField(max_length=10000000)
#     following = models.ManyToManyField(User, related_name='following', blank=True)
    
#     def __str__(self):
#         return str(self.user.username)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=10000)
    post_image = models.ImageField(upload_to='postimages')
    likes = models.ManyToManyField(User, related_name='posts')

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100000)
    category = models.CharField(max_length=1000)
    blog_image = models.ImageField(upload_to='blogimages')
    description = models.CharField(max_length=1000000)
