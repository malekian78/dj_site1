from django.urls import path
from .views import *

app_name = 'website'
urlpatterns = [
    path('', home, name='home'),
    path('contact', contatct, name='myContact'),
    path('testForm1', testingForm1, name='testForm1'),
    path('testForm2', testingForm2, name='testForm2'),
    # path('login/', login_view, name='login')
]
