from django.shortcuts import redirect, render, get_object_or_404
from .models import Post,Comment
from blog.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

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
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in = [kwargs['tag_name']])
    
    #! ______ paginatoring
    #? google search --> django blog pagination for post
    #? https://www.osehfrank.com/en/blog/2020/2/9/create-blog-application-django-part-7-add-pagination-django-blog-9skizlszh5n/
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    
    context = {'posts':posts, "test":30}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, post_id):
    #! روش اول
    # allpost = Post.objects.filter(status=True)
    # thePost = get_object_or_404(allpost, pk= post_id)
    #! روش دوم (که خودم همینو ترجیح میدم)
    if request.method == "POST":
        forms = CommentForm(request.POST)
        if forms.is_valid():
            messages.add_message(request, messages.SUCCESS, 'کامنت شما با موفقیت دریافت شد')
            forms.save()
        else:
            messages.add_message(request, messages.ERROR, 'کامنت شما دریافت نشد')
    thePost = get_object_or_404(Post, pk = post_id, status=True)
    if thePost.login_require and not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('account:login'))
    else:
        comments = Comment.objects.filter(post=thePost.pk,approved=True).order_by('-created_date')
        forms = CommentForm()
        return render(request, 'blog/blog-single.html', {'thePost':thePost,'comments':comments,'forms':forms})

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
