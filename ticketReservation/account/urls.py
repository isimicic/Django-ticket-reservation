from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from .views import LoggedOutView, ProfileView

urlpatterns = [
    url(r'^$', auth_views.login),
    url(r'^register/', CreateView.as_view(
        template_name='account/register.html',
        form_class=UserCreationForm,
        success_url='/'
        )),
    url(r'^login', auth_views.login),
    url(r'^profile/', ProfileView.as_view()),
    url(r'^logout', auth_views.logout, {'next_page': '/account/logged_out'}),
    url(r'^logged_out/', LoggedOutView.as_view()),
]
