"""ticketReservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
# Our views
from .views import IndexView, AboutUsView, ContactView, AccountsProfileView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^city/', include('booking.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/profile', AccountsProfileView.as_view(), name="profile"),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about/$', AboutUsView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
]
