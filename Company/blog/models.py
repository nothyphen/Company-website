from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    def __str__(self):
        return self.title
    

class Article(models.Model):
    STATUS = (
    ('d', 'Draft'),
    ('p', 'Published'),
    )

    category = models.ManyToManyField(Category, blank=True, related_name="articles")
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    describtion = models.TextField()
    thumbnail = models.ImageField(upload_to='static/imgs')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return self.title