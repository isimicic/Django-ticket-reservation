from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.shortcuts import get_list_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from rating.models import Rating
from .models import Movie, City, Screening, Reservation, Seat, ReservationType
from django.utils import timezone
from django.http import HttpResponse
import json


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class MovieView(DetailView):
    """
    Movie View
    """
    template_name = 'booking/movie.html'
    model = Movie
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        """
        :param kwargs: get context data
        :return: movie
        """
        context = super(MovieView, self).get_context_data(**kwargs)
        movie = self.get_object()
        if self.request.user.is_authenticated():
            try:
                context['vote'] = Rating.objects.get(user=self.request.user,
                                                     movie=movie)
            except Rating.DoesNotExist:
                pass
        context['cities'] = get_list_or_404(City.objects.all())

        queryset = Screening.objects.filter(
            auditorium__cinema__city=City.objects.filter()[:1].get())
        context['screenings'] = queryset.filter(
            movie=movie,
            screening_start__gte=timezone.localtime(timezone.now())
        ).order_by('auditorium__cinema__name')

        context['site'] = Site.objects.get_current()
        return context

    def post(self, request, *args, **kwargs):
        data = []
        if request.is_ajax():
            data = Screening.objects.getScreenings(
                request.POST['cityId'],
                request.POST['movieId'])
        return HttpResponse(
            json.dumps(data), content_type='application/json')


class ReserveView(LoginRequiredMixin, DetailView):
    template_name = 'booking/reserve.html'
    model = Screening
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super(ReserveView, self).get_context_data(**kwargs)
        screening = self.get_object()
        context['row_list'] = createRowlist()
        context['seats'] = [s.rowNumber for s in Seat.objects.
                            filter(screenings=screening)]
        context['site'] = Site.objects.get_current()
        return context

    def post(self, request, *args, **kwargs):
        my_list = request.POST['choosen-sits'].split(", ")
        my_list = my_list[:len(my_list)-len(my_list)/2-1]
        screening = self.get_object()
        reservationType = ReservationType.objects.create(type='online')
        cost = request.POST['choosen-cost']
        reservation = Reservation(user=request.user,
                                  reservation_type=reservationType,
                                  screening=screening,
                                  amount=cost)
        reservation.save()
        for item in my_list:
            seat = Seat.objects.create(rowNumber=item,
                                       screenings=screening)
            reservation.seat.add(seat)
        return HttpResponseRedirect(reverse('reserved',
                                    args=(reservation.id,)))


class ReservedView(LoginRequiredMixin, DetailView):
    template_name = 'booking/reserved.html'
    model = Reservation
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super(ReservedView, self).get_context_data(**kwargs)

        context['site'] = Site.objects.get_current()
        return context


def createRowlist():
    import string
    string_list = list(string.uppercase[:12])
    del string_list[7]
    row_list = []
    for alpha in string_list:
        if alpha == "A":
            [row_list.append(alpha+repr(i)) for i in xrange(2, 18)]
            row_list.append(' ')
        elif alpha == "B":
            [row_list.append(alpha+repr(i)) for i in xrange(1, 19)]
            row_list.append(' ')
        elif alpha == "C":
            [row_list.append(alpha+repr(i)) for i in xrange(1, 19)]
            row_list.append(' ')
        elif alpha == "D":
            [row_list.append(alpha+repr(i)) for i in xrange(1, 19)]
            row_list.append(' ')
        elif alpha == "E":
            [row_list.append(alpha+repr(i)) for i in xrange(1, 19)]
            row_list.append(' ')
        elif alpha == "F":
            [row_list.append(alpha+repr(i)) for i in xrange(1, 19)]
            row_list.append(' ')
        elif alpha == "G":
            [row_list.append(alpha+repr(i)) for i in xrange(1, 19)]
            row_list.append(' ')
        elif alpha == "I":
            [row_list.append(alpha+repr(i)) for i in xrange(3, 17)]
            row_list.append(' ')
        elif alpha == "J":
            [row_list.append(alpha+repr(i)) for i in xrange(5, 15)]
            row_list.append(' ')
        elif alpha == "K":
            [row_list.append(alpha+repr(i)) for i in xrange(5, 15)]
            row_list.append(' ')
        elif alpha == "L":
            [row_list.append(alpha+repr(i)) for i in xrange(6, 14)]
            row_list.append(' ')
    return row_list
