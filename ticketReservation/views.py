from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.views.generic import TemplateView
from django.contrib.sites.models import Site
from booking.models import Movie
from rating.models import Rating


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['movies'] = get_list_or_404(Movie.objects.top_rated())

        if self.request.user.is_authenticated():
            votes = Rating.objects.all().filter(
                user=self.request.user)
            context['userVotes'] = votes
        else:
            context['votes'] = Rating.objects.all()
        context['site'] = Site.objects.get_current()
        return context


class AboutUsView(TemplateView):
    template_name = "staticSites/aboutUs.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      {'site': Site.objects.get_current()})


class ContactView(TemplateView):
    template_name = "staticSites/contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      {'site': Site.objects.get_current()})
