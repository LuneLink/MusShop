import json

import decimal
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

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

def itemList(request):
    recieve = json.loads(request.GET.get('send'))

    items = Instrument.objects.filter(type=str(recieve[u'typeId']))\
        .values('id', 'manufacturer__name', 'model', 'type', 'coast')
    print("Items: ")
    print(items)

    json_items = json.dumps(list(items), default=decimal_default)
    print("JSON Items: ")
    print(json_items)

    context = {'content': json_items,
               'pageCount': 1}

    return JsonResponse(context)


def getCurrent(request):
    recieve = json.loads(request.GET.get('send'))

    items = Instrument.objects.filter(type="1", id=recieve[u'currentId'])\
        .values('id', 'manufacturer__name', 'model', 'type', 'coast')
    json_items = json.dumps(list(items), default=decimal_default)
    context = {'content': json_items,
                'information': 'INFOOOO'}

    return JsonResponse(context)


def submitPurchase(request):
    context = {}
    # recieve = request.GET.get('send')
    # print(recieve[u'typeId'])

    return JsonResponse(context)
