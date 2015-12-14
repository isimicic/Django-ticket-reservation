from django.conf.urls import url
from .views import MovieView


urlpatterns = [
    url(r'movie/(?P<slug>\d+)/$', MovieView.as_view(), name='movie'),

]
