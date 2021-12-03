from django.db import models
from apps.blog_articles.models import Articles

# Create your models here.
class Comments(models.Model):
    article_comments = models.ForeignKey(
        Articles, null=True, blank=True, related_name='article_comments',on_delete=models.CASCADE,)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200, blank=True)
    comment_content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.email

  
