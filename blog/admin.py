from django.contrib import admin
from blog.models import Post, Categorie


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Categorie)
