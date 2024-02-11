from django import template
from blog.models import Post,Category
register = template.Library()


@register.simple_tag(name="plus2")
def myfunction(a=2):
    return a + 2

@register.simple_tag
def PostCount():
    postcount = Post.objects.filter(status=1).count()
    return postcount

@register.simple_tag
def allpost():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def myFilter(value,num=30):
    return value[:num]

@register.inclusion_tag('last3postsTEST.html')
def test_last3posts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:3]
    return {'posts': posts}
#!________________________________________________
#! مقدار ۳ تا پست آخر
@register.inclusion_tag('blog/last3blog.html')
def last3posts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:3]
    return {'posts': posts}
#!________________________________________________
#! مقدار دسته بندی ها و تعداد پست هر دسته بندی
@register.inclusion_tag('blog/post-categories.html')
def post_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    print(type(posts))
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}
