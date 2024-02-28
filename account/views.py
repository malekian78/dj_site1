from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #!https://docs.djangoproject.com/en/4.2/topics/auth/default/#module-django.contrib.auth.forms
from django.contrib.auth.decorators import login_required

# ?https://docs.djangoproject.com/en/4.2/topics/auth/

# Create your views here.
def login_view(request): #?https://docs.djangoproject.com/en/4.2/topics/auth/default/#how-to-log-a-user-in
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            # username = request.POST["username"]
            # password = request.POST["password"]
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})

@login_required
def logout_view(request): #?https://docs.djangoproject.com/en/4.2/topics/auth/default/#how-to-log-a-user-out
    logout(request)
    return redirect('/')

def signup_view(request): #? https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.forms.UserCreationForm
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form =  UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('account:login')
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})