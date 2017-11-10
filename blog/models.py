from django.db import models


class Categories(models.Model):
    category_name = models.CharField(max_length=50)
    category_url = models.CharField(max_length=60)
    category_desc = models.TextField()

    def __str__(self):
        return self.category_name


class Post(models.Model):
    post_title = models.CharField(max_length=200, blank=False)
    post_content = models.TextField()
    post_url = models.CharField(max_length=250, blank=False)
    # Many to many field to categories.
    post_category = models.ManyToManyField(Categories)

    def __str__(self):
        return self.post_url
