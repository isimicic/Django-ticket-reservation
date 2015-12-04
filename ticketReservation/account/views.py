#from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class LoggedOutView(TemplateView):
    """ View that will redirect us if we click logout """
    template_name = 'account/logged_out.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    """ View for accessing your account page """
    template_name = 'account/profile.html'
