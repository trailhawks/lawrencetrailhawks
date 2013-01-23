from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    raw_id_fields = ('author',)

admin.site.register(Post, PostAdmin)
