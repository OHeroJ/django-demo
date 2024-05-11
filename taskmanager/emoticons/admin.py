from django.contrib import admin
from .models import Topic, Pic, Mode, Category, Tag, PTag


class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "mode",
        "keywords",
    )
    
class PicAdmin(admin.ModelAdmin):
    list_display = (
        "url",
        "keywords",
    )
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "mode",
    )
    
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "mode",
    )
    
class PTagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
class ModeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    
admin.site.register(Topic, TopicAdmin)
admin.site.register(Pic, PicAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Mode, ModeAdmin)
admin.site.register(PTag, PTagAdmin)

# Register your models here.
