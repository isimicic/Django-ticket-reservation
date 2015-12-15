from django.conf.urls import url
from .views import RatingView

urlpatterns = [
    url(r'^$', RatingView.as_view(), name='rating'),
]
