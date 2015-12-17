from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.contrib.sites.models import Site
# our models
from booking.models import Reservation
from .models import User_profile


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class ProfileIndexView(LoginRequiredMixin, ListView):
    template_name = 'accounts/profile.html'
    model = Reservation

    def get_context_data(self, **kwargs):
        context = super(ProfileIndexView, self).get_context_data(**kwargs)
        context['site'] = Site.objects.get_current()
        return context

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.id)


class AccountEditView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/updateAccount.html'
    model = User
    fields = ['username', 'first_name', 'last_name']
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(AccountEditView, self).get_context_data(**kwargs)
        context['site'] = Site.objects.get_current()
        return context

    def get_object(self):
        return self.model.objects.get(pk=self.request.user.id)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/updateProfile.html'
    model = User_profile
    fields = ['image']
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(ProfileEditView, self).get_context_data(**kwargs)
        context['site'] = Site.objects.get_current()
        return context

    def get_object(self):
        return self.model.objects.get(user=self.request.user.id)
