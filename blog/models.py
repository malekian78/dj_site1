from django.db import models

# Create your models here.
class Post(models.Model):
    # image =
    # author = 
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags = 
    # category = 
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.title

    class Meta: #? https://docs.djangoproject.com/en/4.2/ref/models/options/
        ordering = ['-created_date']
        verbose_name_plural = "پست ها"
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)