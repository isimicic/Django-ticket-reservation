# from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    """ View that will redirect us if we click logout """
    template_name = 'index.html'
