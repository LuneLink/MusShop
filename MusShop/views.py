from django.shortcuts import render

from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):

    types = Type.objects.all()
    context = {'types': types}

    return render(request, 'index.html', context)


def detail(request, type_id):
    return HttpResponse("You're looking at question %s." % type_id)