from django.conf.urls import url  # Django url configuration class.
from blog.views import BlogHomeView  # Importing blog app views


app_name = 'blog'
urlpatterns = [
    url(r'^$', BlogHomeView.as_view(), name='blog_home'),
]
