from django.shortcuts import render


def city(request):
    return render(request, 'booking/city.html', {})
