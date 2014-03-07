from django.conf.urls import patterns, include, url

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
) 


# auth system
urlpatterns += patterns('django.contrib.auth',
    url(r'^sair/$', 'views.logout', {}, 'logout'),
    url(r'^accounts/login/$', 'views.login', {}, 'login'),
)


# DEBUGG
if settings.DEBUG:
    urlpatterns += patterns('',
        # CONTENT MEDIA
        url(r'^media/(.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT }
        ),
        url(r'^static/(.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT }
        ),
    )
