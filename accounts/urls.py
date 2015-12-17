from django.conf.urls import include, url
# Our views
from .views import ProfileIndexView, AccountEditView, ProfileEditView


urlpatterns = [
    url(r'^profile/$', ProfileIndexView.as_view(), name='profile'),
    url(r'^', include('registration.backends.hmac.urls')),
    url(r'^edit/account/$', AccountEditView.as_view(),
        name='editAccount'),
    url(r'^edit/profile/$', ProfileEditView.as_view(),
        name='editProfile'),
]
