from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    post_url = models.CharField(max_length=250)
