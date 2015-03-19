from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import include

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'notes.views.home', name='home'),
#    # url(r'^notes/', include('notes.foo.urls')),
#
#    # Uncomment the admin/doc line below to enable admin documentation:
#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#    # Uncomment the next line to enable the admin:
#    # url(r'^admin/', include(admin.site.urls)),
#)


urlpatterns = patterns('',
    # Examples:
    url(r'^', include('noteme.urls')),
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
