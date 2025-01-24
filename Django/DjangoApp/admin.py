from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Post, Comment

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (None, {'fields': ('birthdate',)})
    )
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (None, {'fields': ('birthdate',)})
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name', 'description', 'icon')
    list_filter = ('author', 'icon')

@admin.register(Post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'author', 'content', 'created')
    list_filter = ('category', 'author', 'created')

@admin.register(Comment)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'content', 'created')
    list_filter = ('post', 'author', 'created')