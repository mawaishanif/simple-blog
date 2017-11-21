from django.db import models
from django.core.exceptions import ValidationError


class Categories(models.Model):
    category_name = models.CharField(max_length=50, blank=False)
    category_url = models.SlugField(max_length=60, unique=True)
    category_desc = models.TextField(blank=True)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        '''
        Overiding save method to call full clean method to avoid empty attributes from saving.
        '''
        self.full_clean()
        super(Categories, self).save(*args, **kwargs)


class Post(models.Model):
    post_title = models.CharField(max_length=200, blank=False)
    post_content = models.TextField(blank=True)
    post_url = models.SlugField(max_length=250, unique=True)

    # Many to many field to categories.
    post_category = models.ManyToManyField(Categories, blank=True)

    def __str__(self):
        return self.post_title

    def save(self, *args, **kwargs):
        '''
        Overiding the save method inorder to call clean method which does not get called by default on custom save function.
        '''
        self.full_clean()
        super(Post, self).save(*args, **kwargs)
