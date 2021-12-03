from django.db import models
from cloudinary.models import CloudinaryField
from apps.blog_categories.models import *

# Create your models here.
class Articles(models.Model):
    category = models.ManyToManyField(
        Categories, null=True, blank=True, related_name='articles')
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    body_content = models.TextField()
    post_image = CloudinaryField('image', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Articles'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

    
