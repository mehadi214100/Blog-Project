from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name','created_at','updated_at')


class blogAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','category','blog_image','status','is_featured')
    prepopulated_fields ={
        'slug':('title',)
    }
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('title','is_featured')


admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Blog,blogAdmin)