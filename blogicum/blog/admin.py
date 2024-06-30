from django.contrib import admin

from .models import Category, Location, Post, User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


if not admin.site.is_registered(User):
    admin.site.register(User)
