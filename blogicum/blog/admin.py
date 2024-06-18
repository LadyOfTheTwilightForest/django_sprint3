from django.contrib import admin
from .models import Category, Location, Post, User

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)
if not admin.site.is_registered(User):
    admin.site.register(User)
