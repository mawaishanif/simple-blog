from django.contrib import admin
from blog.models import Post, Categories


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'post_url': ('post_title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Categories)
