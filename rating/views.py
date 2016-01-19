from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import json
from .models import Rating
from booking.models import Movie


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class RatingView(LoginRequiredMixin, TemplateView):
    """Create Rating View"""

    def post(self, request, *args, **kwargs):
        """
        Post rating
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = {}
        if request.is_ajax():
            movie = get_object_or_404(Movie, id=request.POST['movieId'])
            Rating.objects.create(user=request.user,
                                  rating=request.POST['rating'],
                                  movie=movie)
            avg = movie.get_avg_rating()
            data = {'rating': request.POST['rating'],
                    'avg': avg, 'movieId': request.POST['movieId']}
        return HttpResponse(json.dumps(data))
