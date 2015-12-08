from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
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
        self.publisher = get_object_or_404(self.model)
        return self.model.objects.filter(user=self.request.user.id)
