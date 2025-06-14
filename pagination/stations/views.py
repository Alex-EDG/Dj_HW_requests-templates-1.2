import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_stations = []
    with open(settings.BUS_STATION_CSV, mode='r', encoding='utf-8') as file:
        bus_stations_dict = csv.DictReader(file)
        for station in bus_stations_dict:
            bus_stations.append(station)
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)

    context = {
              'page': page,
              }
    return render(request, 'stations/index.html', context)