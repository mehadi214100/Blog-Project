from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name','created_at','updated_at')



admin.site.register(models.Category,CategoryAdmin)