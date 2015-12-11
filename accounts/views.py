from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
# our models
from booking.models import Reservation


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
        return context

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.id)


class ProfileSettingsView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/updateProfile.html'
    model = User
    fields = ['username', 'first_name', 'last_name']
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.model.objects.get(pk=self.request.user.id)
