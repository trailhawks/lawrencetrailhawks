from __future__ import absolute_import

from django.db import models


# TODO: Add a default manager to only show Public docs.... Mostly needed
# for content_tags.py

class HawkNews(models.Model):
    DRAFT = 1
    PUBLIC = 2
    DRAFT_CHOICES = (
        (DRAFT, "Draft",),
        (PUBLIC, "Public",),
    )
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    draft = models.IntegerField(choices=DRAFT_CHOICES)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "Hawk News"
        verbose_name_plural = "Hawk News"

    def __unicode__(self):
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('news_detail', (), {
            'year': self.start_datetime.strftime("%Y"),
            'month': self.start_datetime.strftime("%b").lower(),
            'day': self.start_datetime.strftime("%d"),
            'slug': self.slug})
