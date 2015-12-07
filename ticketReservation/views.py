# from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class IndexView(TemplateView):
    """ View that will redirect us if we click logout """
    template_name = 'index.html'


class AboutUsView(TemplateView):
    template_name = "aboutUs.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class AccountsProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
