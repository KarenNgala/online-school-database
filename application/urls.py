from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^edit_profile/$', views.profile_edit, name='edit_profile'),
    url(r'^create_unit/$', views.create_unit, name='create_unit'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)