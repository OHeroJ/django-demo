from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # 会在 admin 列表展示
    list_display = ['email', 'username', 'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    ) # 用户编辑
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    ) # 用户添加

admin.site.register(CustomUser, CustomUserAdmin)