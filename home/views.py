from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Plot
import json

# Create your views here.

def get_grid_view(request):
    grid_object = Plot.objects.all()
    return JsonResponse(list(grid_object), safe=False)

def index(request):
    return render(request, 'pages/index.html')

def map_view(request):
    # Example locations
    locations = [
        {"lat": 40.730610, "lng": -73.935242, "name": "New York City"},
        {"lat": 34.052235, "lng": -118.243683, "name": "Los Angeles"},
        {"lat": 41.878113, "lng": -87.629799, "name": "Chicago"},
    ]
    return render(request, "pages/map.html", {"locations": json.dumps(locations)})

def grid_view(request):
    return render(request, 'pages/grid.html')

def settings_view(request):
    return render(request, 'pages/settings.html')
