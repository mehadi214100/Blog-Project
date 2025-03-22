from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .forms import Register,Login
from django.contrib.auth import login,logout

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

def registration(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Register()
    contex = {
        'form':form
    }
    return render(request,'registration.html',contex)


def login_form(request):
    if request.method == 'POST':
        form = Login(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form = Login()
    context = {
        'form':form
    }
    return render(request,'login.html',context)

def logout_user(request):
    logout(request)
    return redirect('/')