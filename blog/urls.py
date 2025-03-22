from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('category/<int:category_id>',views.posts_by_category,name="posts_by_category"),
    path('single_blog/<slug:slug>',views.single_blog,name="single_blog"),
    path('search/',views.search,name="search"),
    path('registration/',views.registration,name="registration"),
    path('login/',views.login_form,name='login'),
    path('logout_user/',views.logout_user,name='logout_user'),
]
