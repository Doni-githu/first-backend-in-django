from django.contrib import admin
from .models import Post, User
# Register your models here.


admin.site.register([Post, User])