import json

import decimal
from math import ceil

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


def splitQuery(queryset):
    count = 6.

    values = list(queryset.all())
    split = int(ceil(len(values) / count))
    print("IN SPLIT")
    print(split)
    columns = [values[i * int(count):(i + 1) * int(count)] for i in range(split)]
    return columns


def itemList(request):
    recieve = json.loads(request.GET.get('send'))
    print("Recieve: ")
    print(recieve)

    if(recieve[u'searchParams'] == {}):
        items = Instrument.objects.filter(type=str(recieve[u'typeId'])) \
            .values('id', 'manufacturer__name', 'model', 'type', 'coast')
    else:
        search = recieve[u'searchParams']
        searchType = search[u'searchType']
        searchValue = search[u'searchValue']

        if(searchType == u'By manufacturer'):
            items = Instrument.objects.filter(type=str(recieve[u'typeId']), manufacturer__name=str(searchValue))\
                .values('id', 'manufacturer__name', 'model', 'type', 'coast')
        if (searchType == u'By model'):
            items = Instrument.objects.filter(type=str(recieve[u'typeId']), model=str(searchValue))\
                                .values('id', 'manufacturer__name', 'model', 'type', 'coast')
        if (searchType == u'By cost'):
            items = Instrument.objects.filter(type=str(recieve[u'typeId']), coast=searchValue)\
                                .values('id', 'manufacturer__name', 'model', 'type', 'coast')

    itemsLength = len(items)
    print("SPLIT")
    print(splitQuery(items))
    print(len(splitQuery(items)))
    splitted = splitQuery(items)

        # items = searchCase[searchType]

    print("Items: ")
    print(items)

    json_items = json.dumps(list(splitted[int(recieve[u'pageId']) - 1]), default=decimal_default)
    print("JSON Items: ")
    print(json_items)

    context = {'content': json_items,
               'pageCount': len(splitted)}

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
