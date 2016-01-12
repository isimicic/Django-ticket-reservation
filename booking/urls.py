from django.conf.urls import url
from .views import MovieView, ReserveView


urlpatterns = [
    url(r'movie/(?P<slug>\d+)/$', MovieView.as_view(), name='movie'),
    url(r'reserve/(?P<slug>\d+)/$', ReserveView.as_view(), name='reserve'),
]
