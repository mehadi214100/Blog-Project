from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name','created_at','updated_at')


class blogAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','category','blog_image','status','is_featured')
    prepopulated_fields ={
        'slug':('title',)
    }


admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Blog,blogAdmin)