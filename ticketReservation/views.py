from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.views.generic import TemplateView
from django.contrib.sites.models import Site
from booking.models import Movie


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['movies'] = get_list_or_404(Movie.objects.all().filter(
            now_playing=True).order_by('-review_grade'))
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
