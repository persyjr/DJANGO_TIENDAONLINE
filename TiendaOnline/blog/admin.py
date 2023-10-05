from django.contrib import admin
from .models import Categoria, Post
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')