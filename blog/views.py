from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>Text from view Home</h1>")
    return render(request, 'myblog/index.html')