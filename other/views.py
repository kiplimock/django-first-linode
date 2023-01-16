from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def simple_view(request):
    return HttpResponse("<h1>This is Django App running in Linode</h1>")