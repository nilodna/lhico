from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    #url(r'^portfolio/', 'core.views.portfolio', name='portfolio'),
    #url(r'^cv/', 'core.views.curriculum', name='curriculum'),
    url(r'^core/static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT, }),
    url(r'^core/media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),
    #url(r'^fotos/', 'core.views.fotos', name='galeria_fotos'),
    #url(r'^videos/', 'core.views.videos', name='galeria_videos'),
    #url(r'^obrigado/', 'core.views.thanks', name='obrigado'),
)