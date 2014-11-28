from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('main.views',
    url(r'^$','principal', name="principal"),
    url(r'^login$', 'login', name="login"),
    url(r'^logout$', 'v_logout', name="v_logout"),
    url(r'^destinos$','destinos', name="destinos"),
    url(r'^buses$', 'buses', name="buses"),
    url(r'^generarorden$', 'generarorden', name="generarorden"),
    url(r'^misdatos$', 'misdatos', name="misdatos"),
    url(r'^registardatos$', 'registardatos', name="registardatos"),
    
    url(r'^admin/', include(admin.site.urls)),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
