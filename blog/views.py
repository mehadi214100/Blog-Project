from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    category = models.Category.objects.all()
    featured_post = models.Blog.objects.filter(is_featured=True, status ='publish').all()
    allpost = models.Blog.objects.filter(is_featured=False,status='publish').all()
    contex = {
        'category':category,
        'featured_post':featured_post,
        'allpost':allpost
    }
    return render(request,'index.html',contex)
