from django.conf.urls import url
from .views import MovieView, ReserveView, ReservedView


urlpatterns = [
    url(r'movie/(?P<slug>\d+)/$', MovieView.as_view(), name='movie'),
    url(r'reserve/(?P<slug>\d+)/$', ReserveView.as_view(), name='reserve'),
    url(r'reserved/(?P<slug>\d+)/$', ReservedView.as_view(), name='reserved'),
]
