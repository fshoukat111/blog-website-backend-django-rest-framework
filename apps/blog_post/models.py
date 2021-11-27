from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from cloudinary.models import CloudinaryField

# Create your models here.
class Categories(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True)
    name = models.CharField(max_length=160, unique=True)
    slug = models.SlugField(max_length=200, blank=True, unique=True)

    class MPTTMeta:
        order_insertion_by = ['id']

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Posts(models.Model):
    category = models.ManyToManyField(
        Categories, null=True, blank=True, related_name='posts')
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    body_content = models.TextField()
    post_image = CloudinaryField('image', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    
