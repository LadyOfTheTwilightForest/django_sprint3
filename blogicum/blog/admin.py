from django.contrib import admin

from .models import Category, Location, Post, User


@admin.register(Category, Location, Post)
class CategoryAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


if not admin.site.is_registered(User):
    admin.site.register(User)
