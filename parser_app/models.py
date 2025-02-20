from django.db import models

class ContentModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    media_type = models.CharField(max_length=50)  # 'movie', 'series', etc.
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title