from django.contrib import admin
from blog.models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

#!https://github.com/summernote/django-summernote?tab=readme-ov-file#apply-summernote-only-to-specific-textfield-in-model 
#!  دقت کنید کلا که نمیشه همزمان از دو کلاس ارث بری کرد
#! ارث بری میکند admin.ModelAdmin استفاده کنیم که خودش میاد از کلاس مادر یعنی  SummernoteModelAdmin اما میشه از کلاس فرزندی به نام  
# class postAdmin(admin.ModelAdmin): 
class postAdmin(SummernoteModelAdmin): 
    #? https://docs.djangoproject.com/en/4.2/ref/contrib/admin/
    date_hierarchy = 'created_date'
    list_display = ("title",'author', 'status', 'login_require', 'published_date', 'updated_date')
    empty_value_display = "_خالی_"
    list_filter = ('status','author')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name',"post",'approved', 'created_date')
    empty_value_display = "_خالی_"
    list_filter = ('post','approved')
    search_fields = ['name', 'post']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Post, postAdmin)
