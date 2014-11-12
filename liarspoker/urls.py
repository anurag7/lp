from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from liarspoker.game import views as gv

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'liarspoker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', gv.index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
