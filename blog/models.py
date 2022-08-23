from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    content = models.TextField()
    image = models.ImageField()
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)