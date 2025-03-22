from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.shortcuts import get_object_or_404
from django.db.models import Q

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

def single_blog(request,slug):
    post = get_object_or_404(models.Blog,slug=slug,status='publish')
    
    return render(request,'singleblog.html',{"post":post})


def search(request):
    keyword = request.GET.get('keyword')
    posts = models.Blog.objects.filter(Q(title__icontains = keyword) | Q(short_desc__icontains = keyword),status='publish')
    context = {
        'keyword':keyword,
        'posts':posts
    }
    return render(request,'search.html',context)