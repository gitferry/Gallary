from django.conf.urls import patterns, include, url
from gallary.views import index, studyList, scienceList, trainList, talentList, allList, info
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', index),
    url(r'^studylist/$', studyList),
    url(r'^info/$', info),
    url(r'^sciencelist/$', scienceList),
    url(r'^trainlist/$', trainList),
    url(r'^talentlist/$', talentList),
    url(r'^alllist/$', allList),
    # Examples:
    # url(r'^$', 'gallary.views.home', name='home'),
    # url(r'^gallary/', include('gallary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    url(r'^tinymce/', include('tinymce.urls')),
)
