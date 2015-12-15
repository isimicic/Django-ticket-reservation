from django.conf.urls import url
# Our views
from .views import ProfileIndexView, AccountEditView, ProfileEditView


urlpatterns = [
    url(r'^$', ProfileIndexView.as_view(), name='profile'),
    url(r'^edit/account/$', AccountEditView.as_view(),
        name='editAccount'),
    url(r'^edit/profile/$', ProfileEditView.as_view(),
        name='editProfile'),
]
