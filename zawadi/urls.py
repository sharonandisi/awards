from django.conf.urls import url , include
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'^projects/(\d+)$', views.image, name='image'),
    url(r'^new-image$', views.new_image, name='new-image'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^profile/(?P<username>\w{0,50})/$', views.profile, name='profile'),
    url(r'^profile_edit/(\d+)$', views.profile_edit, name='edit_profile'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^api/profiles/$', views.ListProfiles.as_view()),
    url(r'^api/images/$', views.ListImages.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
