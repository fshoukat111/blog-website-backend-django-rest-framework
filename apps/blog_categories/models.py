from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

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