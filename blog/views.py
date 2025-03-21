from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.shortcuts import get_object_or_404
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

def posts_by_category(request,category_id):
    posts = models.Blog.objects.filter(status='publish',category=category_id)
    # try:
    #     categorys = models.Category.objects.get(id=category_id)
    # except:
    #     return redirect('/')

    categorys = get_object_or_404(models.Category,pk=category_id)

    contex = {
        'posts':posts,
        'categorys':categorys
    }
    return render(request,'posts_by_category.html',contex)