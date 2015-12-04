from django.contrib import admin
from models import *

admin.site.register(Movie)

admin.site.register(Auditorium)
admin.site.register(Seat)
admin.site.register(ReservationType)
admin.site.register(Reservation)
admin.site.register(Screening)
admin.site.register(SeatReserved)


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'auditorium_number', 'city')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
