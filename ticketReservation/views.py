# from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """ View that will redirect us if we click logout """
    template_name = 'index.html'


class AboutUsView(TemplateView):
    template_name = "aboutUs.html"


class ContactView(TemplateView):
    template_name = "contact.html"
