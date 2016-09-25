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


def ajaxTest(request):
    context = {}

    return render(request, "itemList.html", context)
    # return render(request, "itemList.html", context)


def bucketOpen(request):
    context = {'info' : 'some info'}

    return render(request, "bucketList.html", context)

def getCurrent(request):
    context = {}

    return render(request, "currentItem.html", context)
