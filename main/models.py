from django.db import models


class News(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='news_img', blank=True, null=True)

    def __str__(self):
        return self.title