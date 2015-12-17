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
            try:
                context['vote'] = Rating.objects.get(user=self.request.user,
                                                     movie=self.get_object())
            except Rating.DoesNotExist:
                pass
        context['site'] = Site.objects.get_current()
        return context
