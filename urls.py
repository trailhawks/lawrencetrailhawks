from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from lawrencetrailhawks.lib.Extras import get_latest


admin.autodiscover()


def redirect(url):
    def inner(request):
        return HttpResponseRedirect(url)
    return inner


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', direct_to_template, {'template': 'homepage.html',
                                 'extra_context': get_latest(),
                                }),
    (r'^live/$', direct_to_template, {'template': 'live_coverage.html'}),
    (r'^photos/', include('lawrencetrailhawks.photos.urls.photos')),
    (r'^about/$', direct_to_template, {'template': 'about.html'}),
    (r'^faq/', include('lawrencetrailhawks.faq.urls.faq')),
    (r'^blog/', include('lawrencetrailhawks.blog.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^links/', include('lawrencetrailhawks.links.urls.links')),
    (r'^runs/', include('lawrencetrailhawks.runs.urls.runs')),
    (r'^members/', include('lawrencetrailhawks.members.urls.members')),
    (r'^sponsors/', 'lawrencetrailhawks.sponsors.views.get_sponsors'),
    (r'^races/', include('lawrencetrailhawks.races.urls.races')),
    #(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    #        {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^contact/$', 'lawrencetrailhawks.members.views.officer_list'),
    (r'^thanks/$', direct_to_template, {'template': 'thanks.html'}),
    (r'^member_list/$', 'lawrencetrailhawks.lth.views.member_list'),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    )
