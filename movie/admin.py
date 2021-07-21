from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Category, Director, Comment, Movie

# Register your models here.

class CategoryAdmin(ModelAdmin):

    list_display = ('name',)

    prepopulated_fields = {"slug": ("name",)}

class DirectorAdmin(ModelAdmin):

    list_display = ('name', 'created')

    prepopulated_fields = {"slug": ("name",)}

class MovieAdmin(ModelAdmin):

    list_display = ('name', 'categories', 'created', 'updated')

    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Comment)
admin.site.register(Movie, MovieAdmin)
