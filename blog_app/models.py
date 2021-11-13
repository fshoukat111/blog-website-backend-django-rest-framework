from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Categories(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True)
    name = models.CharField(max_length=160, unique=True)
    slug = models.SlugField(max_length=200, blank=True,unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']


class Posts(models.Model):
    category  = models.ForeignKey(Categories,null=True, blank=True,related_name='posts',on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, blank=True,unique=True)
    body_content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title;
    
    class Meta:
        ordering = ['created']

