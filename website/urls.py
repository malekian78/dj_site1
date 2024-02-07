from django.urls import path
from .views import *

app_name = 'website'
urlpatterns = [
    path('', home, name='home'),
    path('contact', contatct, name='myContact'),
    # path('login/', login_view, name='login')
]
