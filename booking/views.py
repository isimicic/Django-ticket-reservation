from django.views.generic import DetailView
from django.contrib.sites.models import Site
from .models import Movie
from rating.models import Rating


class MovieView(DetailView):
    template_name = 'booking/movie.html'
    model = Movie
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super(MovieView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['vote'] = Rating.objects.get(user=self.request.user,
                                                 movie=context['object'])
        context['site'] = Site.objects.get_current()
        return context
