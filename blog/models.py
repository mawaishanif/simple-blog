from django.db import models
from django.core.exceptions import ValidationError


class Categorie(models.Model):
    name = models.CharField(max_length=50, blank=False)
    url = models.SlugField(max_length=60, unique=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        '''
        Overiding save method to call full clean method to avoid empty attributes from saving.
        '''
        self.full_clean()
        super(Categorie, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=True)
    url = models.SlugField(max_length=250, unique=True)

    # Many to many field to categories.
    category = models.ManyToManyField(Categorie, blank=True)

    def __str__(self):
        return self.post_title

    def save(self, *args, **kwargs):
        '''
        Overiding the save method inorder to call clean method which does not get called by default on custom save function.
        '''
        self.full_clean()
        super(Post, self).save(*args, **kwargs)
