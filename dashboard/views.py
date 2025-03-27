from django.shortcuts import render,redirect
from blog.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import categoryForm,postForm
from django.template.defaultfilters import slugify
from django.http import HttpResponse
from .decorators import manager_required,editor_required,author_required
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.contrib.auth import update_session_auth_hash

@login_required
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    print(request.path)
    context = {
        'category_count':category_count,
        'blog_count':blog_count

    }
    return render(request,'dashboard.html',context)

@manager_required
def categories(request):
    return render(request,'categories.html')

def add_categories(request):
    if request.method == 'POST':
        form = categoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = categoryForm()
    contex = {
        'form':form
    }
    return render(request,'add_categories.html',contex)


def edit_categories(request,id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = categoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = categoryForm(instance=category)
    contex = {
        'form':form
    }
    return render(request,'add_categories.html',contex)

def delete_categories(request,id):
    cate = Category.objects.get(id=id)
    cate.delete()
    return redirect('categories')

@editor_required
def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'posts.html',context)

def add_post(request):
    if request.method == 'POST':
        form = postForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            return redirect('posts')
    else:
        form = postForm()
    contex = {
        'form':form
    }
    return render(request,'add_post.html',contex)


def edit_post(request,id):
    post = Blog.objects.get(id=id)
    if request.method == 'POST':
        form = postForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            return redirect('posts')
    else:
        form = postForm(instance=post)
    contex = {
        'form':form
    }
    return render(request,'add_post.html',contex)


def delete_post(request,id):
    post = Blog.objects.get(id=id)
    post.delete()
    return redirect('posts')

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data = request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        'form':form
    }
    return render(request,'pass_change.html',context)