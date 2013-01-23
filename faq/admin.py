from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import FAQ


class FaqInline(generic.GenericStackedInline):
    model = FAQ
    extra = 0


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'content_type')


admin.site.register(FAQ, FaqAdmin)
