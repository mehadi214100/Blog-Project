from django import forms
from blog.models import Category

class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'