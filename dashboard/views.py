from django.shortcuts import render,redirect
from blog.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import categoryForm
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


def categories(request):
    print(request.path)
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