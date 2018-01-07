from django.conf.urls import url

from . import views

app_name = 'music'
urlpatterns = [
	# /music/
	url(r'^$', views.IndexView.as_view(), name='index'),

	url(r'^register/$', views.UserFormView.as_view(), name='register'),

	# /music/712/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

	# /music/album/add/
	url(r'album/add/$', views.AlbumCreateView.as_view(), name='album-add'),

	# /music/album/2/
	url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdateView.as_view(), name='album-update'),

	# /music/album/2/delete/
	url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDeleteView.as_view(), name='album-delete'),
]