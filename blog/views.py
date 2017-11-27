from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post


class BlogHomeView(TemplateView):
    template_name = 'blog/blog-home.html'

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        context['latest_articles'] = Post.objects.all()[:5]
        categories = {}
        for post in context['latest_articles']:
            setattr(post, 'categorie', post.category.all()[0])
        return context
