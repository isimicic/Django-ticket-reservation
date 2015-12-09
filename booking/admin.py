from django.contrib import admin
from imagekit.admin import AdminThumbnail
from .models import *


admin.site.register(Auditorium)
admin.site.register(Seat)
admin.site.register(ReservationType)
admin.site.register(Reservation)
admin.site.register(Screening)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='image_thumbnail')


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'auditorium_number', 'city')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
