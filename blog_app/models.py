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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'


class Posts(models.Model):
    category = models.ManyToManyField(
        Categories, null=True, blank=True, related_name='posts')
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    body_content = models.TextField()
    post_image = CloudinaryField('image', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'
    


class Comments(models.Model):
    comment_posts = models.ForeignKey(
        Posts, null=True, blank=True, related_name='comment_posts',on_delete=models.CASCADE,)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200, blank=True, unique=True)
    message_comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-created']
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'


