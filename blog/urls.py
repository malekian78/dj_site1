from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('myblog', myblog, name='myblog'),
    path('', blog_view, name='blogView'),
    path('single/<int:post_id>', blog_single, name='single'),
    path('category/<str:cat_name>', blog_view, name='category'),
    path('tag/<str:tag_name>', blog_view, name='tag'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('search/', blog_search, name='search'),
    # path('login/', login_view, name='login')
]
