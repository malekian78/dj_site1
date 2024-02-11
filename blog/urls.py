from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('myblog', myblog, name='myblog'),
    path('', blog_view, name='blogView'),
    path('single/<int:post_id>', blog_single, name='single'),
    path('category/<str:cat_name>', blog_view, name='category'),
    # path('login/', login_view, name='login')
]
