from django.shortcuts import render

def blog_view(request):
    # return HttpResponse("<h1>Text from view Home</h1>")
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    return render(request, 'blog/blog-single.html')

def myblog(request):
    return render(request, 'myblog/index.html')
