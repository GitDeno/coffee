from django.db import models
from django.utils import timezone

# Model for blog posts
class Post(models.Model):
    title = models.CharField(max_lenght=250)
    slug = models.SlugField(max_lenght=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

