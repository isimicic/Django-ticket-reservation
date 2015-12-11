from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.sites.models import Site


class IndexView(TemplateView):
    template_name = 'staticSites/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      {'site': Site.objects.get_current()})


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
