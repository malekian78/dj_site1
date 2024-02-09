from django.contrib import admin
from blog.models import Post

# Register your models here.

class postAdmin(admin.ModelAdmin): #? https://docs.djangoproject.com/en/4.2/ref/contrib/admin/
    date_hierarchy = 'created_date'
    list_display = ('pk',"title",'author', 'status', 'published_date', 'updated_date')
    empty_value_display = "_خالی_"
    list_filter = ('status','author')
    search_fields = ['title', 'content']
    

admin.site.register(Post, postAdmin)
