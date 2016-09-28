from django.http import JsonResponse
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


def itemList(request):
    context = {'message': "GET OUT!",
               'content': [
                   {
                        'id': 1,
                        'manufacturer': 'Jackson',
                        'model': 'KingV',
                        'cost': 100
                   },
                   {
                       'id': 2,
                       'manufacturer': 'Jackson',
                       'model': 'Dinky DK2',
                       'cost': 100
                   },
                   {
                       'id': 3,
                       'manufacturer': 'Jackson',
                       'model': 'Dinky DK7-M',
                       'cost': 100
                   },
                   {
                       'id': 4,
                       'manufacturer': 'Jackson',
                       'model': 'Minion',
                       'cost': 100
                   }
               ]}
    print(request.GET.get('send'))
    return JsonResponse(context)
    # return render(request, "test.html", context)


def getCurrent(request):
    context = {'information': 'Some awesome information',
               'id': int(request.GET.get('send')),
               'cost': 100,
               'manufacturer': 'Jackson',
               'model': 'KingV'}

    return JsonResponse(context)
