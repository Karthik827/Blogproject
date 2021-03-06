from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (('drafts','Drafts'),('published','Published'))
    title = models.CharField(max_length=65)
    slug = models.SlugField(max_length=264 ,unique_for_date='publish')
    author = models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
