from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

handler404 = "cmsproject.views.page_not_found"
handler500 = "cmsproject.views.server_error"

sitemaps = {
#    'news': NewsEntrySitemap,
}

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^robots.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain',}),
#    (r'^crossdomain.xml$', direct_to_template, {'template': 'crossdomain.xml', 'mimetype': 'application/xml',}),
)

if settings.IS_DEV_SERVER:
    urlpatterns = patterns('',
        #(r'^' + settings.MEDIA_URL.lstrip('/') + '(?P<file>.*.htc)$', 'devserver.views.put_file', {'media_root': settings.MEDIA_ROOT, 'mimetype': "text/x-component"}),
        (r'^' + settings.MEDIA_URL.lstrip('/') + '(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^500/$', handler500),
    ) + urlpatterns
    if 'appmedia' in settings.INSTALLED_APPS:
        urlpatterns = patterns('',
            (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
        ) + urlpatterns
    if settings.IS_HTTP_SERVER:
        urlpatterns = patterns('',
            (r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + '../', 'show_indexes': True}),
        ) + urlpatterns

if settings.USE_I18N:
    urlpatterns = patterns('',
        (r'^i18n/setlang/$', 'django.views.i18n.set_language'),
    ) + urlpatterns

if 'django.contrib.sitemaps' in settings.INSTALLED_APPS:
    urlpatterns = patterns('',
        (r'^sitemap.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemaps}),
        (r'^sitemap-(?P<section>.+).xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    ) + urlpatterns

if 'blogposts' in settings.INSTALLED_APPS:
    urlpatterns = patterns('',
        (r'^blog/', include('blogposts.urls')),
    ) + urlpatterns

if 'newsletter' in settings.INSTALLED_APPS:
    urlpatterns = patterns('',
        (r'^newsletter/', include('newsletter.urls')),
    ) + urlpatterns

if 'tinymce' in settings.INSTALLED_APPS:
    urlpatterns = patterns('',
        (r'^tinymce/', include('tinymce.urls')),
    ) + urlpatterns
    
#if 'news' in settings.INSTALLED_APPS:
#    urlpatterns = patterns('',
#        (r'^news/', include('news.urls')),
#    ) + urlpatterns

if 'events' in settings.INSTALLED_APPS:
    urlpatterns = patterns('',
        (r'^events/', include('events.urls')),
    ) + urlpatterns

if 'contactform' in settings.INSTALLED_APPS:
    urlpatterns = patterns('',
        (r'^contactform/', include('contactform.urls')),
    ) + urlpatterns

if 'gallery' in settings.INSTALLED_APPS:
    urlpatterns = patterns('',
        (r'^gallery/', include('gallery.urls')),
    ) + urlpatterns

if 'csv_export' in settings.INSTALLED_APPS:
    urlpatterns = patterns('csv_export.views',
        (r"^admin/(?P<app_label>\w+)/(?P<model_name>\w+)/csv/$", "export"), # Return a CSV file for this model
    ) + urlpatterns

if 'siteinfo' in settings.INSTALLED_APPS:
    urlpatterns = patterns('',
        (r"^siteinfo/", include('siteinfo.urls')),
    ) + urlpatterns

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns = patterns('',
        (r'^rosetta/', include("rosetta.urls")),
    ) + urlpatterns
    
if 'newsletter' in settings.INSTALLED_APPS:
    urlpatterns = patterns('',
        (r'^newsletters/', include('newsletter.urls')),
    ) + urlpatterns


# cms urls must be the last pattern!
if 'cms' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'', include('cms.urls')),
    )
