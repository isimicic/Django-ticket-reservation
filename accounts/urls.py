from django.conf.urls import url
# Our views
from .views import ProfileIndexView


urlpatterns = [
    url(r'^$', ProfileIndexView.as_view(), name='profile'),
]
