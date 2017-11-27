from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
from django.views.generic.dates import YearArchiveView


class BlogHomeView(TemplateView):
    template_name = 'blog/blog-home.html'

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        context['latest_articles'] = Post.objects.all()[:5]
        categories = {}
        for post in context['latest_articles']:
            setattr(post, 'categorie', post.category.all()[0])
        return context


class PostYearArchiveView(YearArchiveView):
    queryset = Post.objects.all()
    date_field = "creation_date"
    make_object_list = True
