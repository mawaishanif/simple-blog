from django.conf.urls import url  # Django url configuration class.
from blog.views import BlogHomeView  # Importing blog app views
from django.views.generic.dates import ArchiveIndexView
from blog.views import PostYearArchiveView, BlogPostView
from blog.models import Post


app_name = 'blog'
urlpatterns = [
    url(r'^$', BlogHomeView.as_view(), name='blog_home'),
    url(r'^archive/$', ArchiveIndexView.as_view(model=Post, date_field='creation_date'), name='post_archive'),
    url(r'^(?P<year>[0-9]{4})/$', PostYearArchiveView.as_view(), name="article_year_archive"),
    url(r'^(?P<slug>[\w-]+)', BlogPostView.as_view(), name='blog_post')
]
