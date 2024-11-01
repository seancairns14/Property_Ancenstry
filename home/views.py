from django.shortcuts import render
from django.http import HttpResponse
from .models import Plot

# Create your views here.


def grid_view(request):
    return render(request, 'grid/grid.html')