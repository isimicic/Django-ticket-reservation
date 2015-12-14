from django.views.generic import DetailView
from .models import Movie


class MovieView(DetailView):
    template_name = 'booking/movie.html'
    model = Movie
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super(MovieView, self).get_context_data(**kwargs)
        return context
