from django.shortcuts import render, get_object_or_404
from .models import Post

# def blog_view(request, cat_name=None, author_username = None):
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=True)
    # if cat_name:
    #     posts = posts.filter(category__name=cat_name)
    # if author_username:
    #     posts = posts.filter(author__username = author_username)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    context = {'posts':posts, "test":30}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, post_id):
    #! روش اول
    # allpost = Post.objects.filter(status=True)
    # thePost = get_object_or_404(allpost, pk= post_id)
    #! روش دوم (که خودم همینو ترجیح میدم)
    thePost = get_object_or_404(Post, pk = post_id, status=True)
    return render(request, 'blog/blog-single.html', {'thePost':thePost}) 

def blog_search(request):
    print(request.__dict__)
    print(request)
    posts = Post.objects.filter(status=True)
    if request.method == "GET":
        posts = posts.filter(content__contains = request.GET.get('s'))
    context = {'posts':posts, "test":30}
    return render(request, 'blog/blog-home.html', context)

def myblog(request):
    # return HttpResponse("<h1>Text from view Home</h1>")
    return render(request, 'myblog/index.html')
