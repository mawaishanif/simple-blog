from django.db import models
from django.core.exceptions import ValidationError


class Categories(models.Model):
    category_name = models.CharField(max_length=50)
    category_url = models.SlugField(max_length=60, unique=True)
    category_desc = models.TextField(blank=True)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    post_title = models.CharField(max_length=200, blank=False)
    post_content = models.TextField(blank=True)
    post_url = models.SlugField(max_length=250, unique=True)
    # Many to many field to categories.
    post_category = models.ManyToManyField(Categories, blank=True)

    def __str__(self):
        return self.post_title
