from typing import Any
from django.contrib import admin
from django.http import HttpRequest

from tasks.models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', "owner",'created_at', 'updated_at')
    list_filter = ('status',)
    actions = ['mark_archived']
    def mark_archived(self, request, queryset):
        # queryset 包含管理员用户从列表中选择的所有任务
        queryset.update(status='ARCHIVED')
        
        
    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        if  request.user.has_perm('tasks.change_task'):
            return True 
        return False

    def has_add_permission(self, request: HttpRequest) -> bool:
        if  request.user.has_perm('tasks.add_task'):
            return True 
        return False
    
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        if  request.user.has_perm('tasks.delete_task'):
            return True 
        return False
        
    mark_archived.short_description = 'Mark selected tasks as archived'
    
admin.site.register(Task, TaskAdmin)