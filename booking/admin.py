from django.contrib import admin
from imagekit.admin import AdminThumbnail
from .models import *
from rating.models import Rating


@admin.register(Auditorium)
class AuditoriumAdmin(admin.ModelAdmin):
    list_display = ('name', 'seats_number')
    list_filter = ('name', 'seats_number')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',
                    'auditorium_number', 'get_city_name')
    list_filter = ('name', 'address', 'auditorium_number')

    def get_city_name(self, obj):
        return obj.city.name


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


class RatingInline(admin.StackedInline):
    """Rating Inline."""
    model = Rating
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [RatingInline]
    list_display = ('title', 'director', 'duration', 'movie_thumbnail')
    list_filter = ('title', 'director', 'duration')
    movie_thumbnail = AdminThumbnail(image_field='image_thumbnail')


@admin.register(ReservationType)
class ReservationTypeAdmin(admin.ModelAdmin):
    list_display = ('type', )


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_date', 'reserved', 'paid', 'active',
                    'get_reservation_type', 'get_user',
                    'get_screening')
    list_filter = ('reservation_date', 'reserved', 'paid', 'active')
    actions = ['make_paid']

    def get_reservation_type(self, obj):
        return obj.reservation_type.type

    def get_user(self, obj):
        return obj.user.username

    def get_screening(self, obj):
        return obj.screening.id

    def make_paid(self, request, queryset):
        rows_updated = queryset.update(paid=True, active=True, reserved=True)
        if rows_updated == 1:
            message_bit = "1 reservation was"
        else:
            message_bit = "%s reservations were" % rows_updated
        self.message_user(
            request, "%s successfully marked as paid." % message_bit)
    make_paid.short_description = "Mark selected reservation as paid"


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('row', 'number', 'get_auditorium_name')
    list_filter = ('row', 'number')

    def get_auditorium_name(self, obj):
        return obj.auditorium.name
