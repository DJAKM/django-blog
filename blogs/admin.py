from django.contrib import admin
from .models import Category,Blog

class CategoryView(admin.ModelAdmin):
    list_display = ("category_name","updated_at","created_at")


class BlogsAdmin(admin.ModelAdmin):
    list_display=('title','author','status','is_featured','created_at','updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields=('title','author','status','category__category_name')
    list_editable= ('is_featured',)
    sortable_by=('title','is_featured')
# Register your models here.
admin.site.register(Category,CategoryView)
admin.site.register(Blog,BlogsAdmin)