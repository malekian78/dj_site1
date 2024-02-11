from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_view(request, cat_name=None):
    posts = Post.objects.filter(status=True)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    context = {'posts':posts, "test":30}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, post_id):
    #! روش اول
    # allpost = Post.objects.filter(status=True)
    # thePost = get_object_or_404(allpost, pk= post_id)
    #! روش دوم (که خودم همینو ترجیح میدم)
    thePost = get_object_or_404(Post, pk = post_id, status=True)
    return render(request, 'blog/blog-single.html', {'thePost':thePost}) 

def myblog(request):
    # return HttpResponse("<h1>Text from view Home</h1>")
    return render(request, 'myblog/index.html')
