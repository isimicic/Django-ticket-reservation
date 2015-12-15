from django.views.generic import DetailView
from django.contrib.sites.models import Site
from .models import Movie


class MovieView(DetailView):
    template_name = 'booking/movie.html'
    model = Movie
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super(MovieView, self).get_context_data(**kwargs)
        context['site'] = Site.objects.get_current()
        return context
