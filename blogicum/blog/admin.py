from django.contrib import admin
# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)
if not admin.site.is_registered(User):
    admin.site.register(User)


