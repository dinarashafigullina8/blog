from django.contrib import admin
from core.models import Category, Post, User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text', 'date')
    list_display_links = ('topic',)
    search_fields = ('topic', 'date')

class UserAdmin(admin.ModelAdmin):
    list_display = ('post', 'first_name', 'last_name', 'gender', 'email', 'about', 'photo')
    search_fields = ('first_name', 'last_name', 'gender', 'email')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)