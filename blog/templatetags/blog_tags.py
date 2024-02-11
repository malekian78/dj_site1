from django import template
from blog.models import Post
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

@register.inclusion_tag('last3posts.html')
def last3posts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:3]
    return {'posts': posts}
