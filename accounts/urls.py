from django.conf.urls import url
# Our views
from .views import ProfileIndexView, ProfileSettingsView


urlpatterns = [
    url(r'^$', ProfileIndexView.as_view(), name='profile'),
    url(r'^settings/$', ProfileSettingsView.as_view(),
        name='profile_settings'),
]
