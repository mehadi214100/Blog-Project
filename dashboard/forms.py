from django import forms
from blog.models import Category,Blog

class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class postForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','category','blog_image','short_desc','blog_body','status','is_featured')

