from django.contrib import admin

from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_files = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name',)
    list_display_links = ('id', 'name',)
    search_files = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)