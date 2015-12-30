from django.views.generic import DetailView, TemplateView
from django.contrib.sites.models import Site
from django.shortcuts import get_list_or_404
from rating.models import Rating
from .models import Movie, City, Screening
from django.utils import timezone
from django.http import HttpResponse
import json


class MovieView(DetailView):
    template_name = 'booking/movie.html'
    model = Movie
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super(MovieView, self).get_context_data(**kwargs)
        movie = self.get_object()
        if self.request.user.is_authenticated():
            try:
                context['vote'] = Rating.objects.get(user=self.request.user,
                                                     movie=movie)
            except Rating.DoesNotExist:
                pass
        context['cities'] = get_list_or_404(City.objects.all())

        queryset = Screening.objects.filter(
            auditorium__cinema__city=City.objects.filter()[:1].get())
        context['screenings'] = queryset.filter(
            movie=movie,
            screening_start__gte=timezone.localtime(timezone.now())
        ).order_by('auditorium__cinema__name')

        context['site'] = Site.objects.get_current()
        return context

    def post(self, request, *args, **kwargs):
        data = []
        if request.is_ajax():
            data = Screening.objects.getScreenings(
                request.POST['cityId'],
                request.POST['movieId'])

        return HttpResponse(
            json.dumps(data), content_type='application/json')


class ReserveView(TemplateView):
    template_name = 'booking/reserve.html'

    def get_context_data(self, **kwargs):
        context = super(ReserveView, self).get_context_data(**kwargs)

        context['site'] = Site.objects.get_current()
        return context
