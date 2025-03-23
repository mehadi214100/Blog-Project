from django.urls import path
from .import views
urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('categories/',views.categories,name="categories"),
    path('categories/add/',views.add_categories,name="add_categories"),
    path('categories/edit_categories/<int:id>',views.edit_categories,name="edit_categories"),
    path('categories/delete_categories/<int:id>',views.delete_categories,name="delete_categories"),
    path('posts/',views.posts,name="posts"),
    path('posts/add',views.add_post,name="add_post"),
    path('posts/edit_post/<int:id>',views.edit_post,name="edit_post"),
    path('posts/delete_post/<int:id>',views.delete_post,name="delete_post"),
]
