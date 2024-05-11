from django.contrib import admin
from .models import Topic, Pic, Mode, Category, Tag

admin.site.register([Topic, Pic, Mode, Category, Tag])

# Register your models here.
