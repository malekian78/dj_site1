from django.contrib import admin
from blog.models import Post

# Register your models here.

class postAdmin(admin.ModelAdmin): #? https://docs.djangoproject.com/en/4.2/ref/contrib/admin/
    list_display = ('pk',"title", 'status', 'published_date', 'created_date', 'updated_date')

admin.site.register(Post, postAdmin)
