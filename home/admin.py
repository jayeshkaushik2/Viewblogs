from django.contrib import admin
from home.models import Blog, Contact, Post, User_profile

# Register your models here.
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(User_profile)