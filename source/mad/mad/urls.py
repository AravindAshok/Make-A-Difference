from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'makeadifference.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'mad.views.login'),
    url(r'^accounts/auth/$', 'mad.views.auth_view'),
    url(r'^accounts/logout/$', 'mad.views.logout'),
    url(r'^accounts/loggedin/$', 'mad.views.loggedin'),
    url(r'^accounts/invalid/$', 'mad.views.invalidlogin'),
)
