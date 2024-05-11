from django.contrib import admin
from .models import Topic, Pic, Mode, Category, Tag, PTag

admin.site.register([Topic, Pic, Mode, Category, Tag, PTag])

# Register your models here.
