from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

