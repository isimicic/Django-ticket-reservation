from django.conf.urls import url
# Our views
from .views import ProfileIndexView, ProfileSettingsView


urlpatterns = [
    url(r'^$', ProfileIndexView.as_view(), name='profile'),
    url(r'^edit/$', ProfileSettingsView.as_view(),
        name='edit'),
]
