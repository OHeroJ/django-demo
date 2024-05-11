from django.db import models
from django.conf import settings

# Create your models here.
class Mode(models.Model):
    name = models.CharField(max_length=50, verbose_name="名称")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "类型"
        verbose_name_plural = "类型"

    
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="分类名称")
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    def __str__(self) -> str:
        return self.name + "("+ self.mode.name + ")"
    
    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"

    
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name + "("+ self.mode.name + ")"
    
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"

class PTag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "图片标签"
        verbose_name_plural = "图片标签"
    
class Pic(models.Model):
    keywords = models.CharField(max_length=100, null=True, blank=True, verbose_name='关键词，用于搜索')
    tags = models.ManyToManyField(PTag, related_name='pic_tag')
    url = models.URLField(verbose_name='图片链接')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    no_words = models.BooleanField(default=False, verbose_name="无字")
    blur_hash = models.CharField(max_length=256, null=True, blank=True)
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE, related_name='pics')
    
    class Meta:
        verbose_name = "图片"
        verbose_name_plural = "图片"
    
        
class Topic(models.Model):
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100, null=True, blank=True, help_text='用于搜索')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='topic_tag')
    pics = models.ManyToManyField(Pic, related_name='topics')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("topic_detail", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name = "话题"
        verbose_name_plural = "话题"
 


    