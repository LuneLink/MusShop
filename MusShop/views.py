import json

import decimal
from math import ceil

from django.http import JsonResponse
from django.shortcuts import render

from django.http import HttpResponse
from pymongo import MongoClient
from rest_framework import viewsets

from MusShop.serializers import *
from .models import *

from tasks import *

import redis
import mongo
# REST api


class InstrumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Instrument to be viewed or edited.
    """
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Instrument to be viewed or edited.
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Instrument to be viewed or edited.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class SizeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Instrument to be viewed or edited.
    """
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


#  views

class MyRedis:
    r_server = None

    @staticmethod
    def redis_init(self):
        print "redis init"
        self.r_server = redis.Redis('localhost')  # this line creates a new Redis object and
        # connects to our redis server
        self.r_server.set('index_counter', 0)
        self.r_server.set('itemList_counter', 0)
        self.r_server.set('getCurrent_counter', 0)
        # r_server.set('test_key', 'test_value')  # with the created redis object we can
        # # submits redis commands as its methods
        # print 'previous set key ' + r_server.get('test_key')  # the previous set key is fetched

    @staticmethod
    def getServer(self):
        if(self.r_server == None):
            self.redis_init(self)

        return self.r_server


def index(request):
    r_server = MyRedis.getServer(self=MyRedis)
    r_server.incr('index_counter')

    types = Type.objects.all()
    context = {'types': types}

    print 'Index total count ' + r_server.get('index_counter')
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
    connection = mongo.Mongo()

    r_server = MyRedis.getServer(self=MyRedis)
    r_server.incr('itemList_counter')

    recieve = json.loads(request.GET.get('send'))
    print("Recieve: ")
    print(recieve)

    if(recieve[u'searchParams'] == {}):
        # items = Instrument.objects.filter(type=str(recieve[u'typeId'])) \
        #     .values('id', 'manufacturer__name', 'model', 'type', 'coast')
        json_items = json.dumps(connection.getInstrumentsByType(str(recieve[u'typeId'])))  # mongo
        # items = connection.getInstrumentsByType(str(recieve[u'typeId']))  # mongo
    else:
        search = recieve[u'searchParams']
        searchType = search[u'searchType']
        searchValue = search[u'searchValue']

        if(searchType == u'By manufacturer'):
            # items = Instrument.objects.filter(type=str(recieve[u'typeId']), manufacturer__name=str(searchValue))\
            #     .values('id', 'manufacturer__name', 'model', 'type', 'coast')
            json_items = json.dumps(connection.getInstrumentByManufacturer(str(searchValue)))
        if (searchType == u'By model'):
            # items = Instrument.objects.filter(type=str(recieve[u'typeId']), model__search=str(searchValue))\
            #                     .values('id', 'manufacturer__name', 'model', 'type', 'coast')
            json_items = json.dumps(connection.getInstrumentByModel(str(searchValue)))
        if (searchType == u'By cost'):
            # items = Instrument.objects.filter(type=str(recieve[u'typeId']), coast=searchValue)\
            #                     .values('id', 'manufacturer__name', 'model', 'type', 'coast')
            json_items = json.dumps(connection.getInstrumentByCost(str(searchValue)))

    # itemsLength = len(items)
    # print("SPLIT")
    # print(splitQuery(items))
    # print(len(splitQuery(items)))
    # splitted = splitQuery(items)

        # items = searchCase[searchType]

    # print("Items: ")
    # print(items)

    # json_items = json.dumps(list(splitted[int(recieve[u'pageId']) - 1]), default=decimal_default)
    # print("JSON Items: ")
    # print(json_items)
    # print "HERE I AM"
    # for document in items:
    #     print document
    # context = {'content': items,
    #            'pageCount': 1}
    # connection.insertInstrument()


    # print "HERE I AM"
    # print json_items
    # for document in json_items:
    #     print document
    context = {'content': json_items,
               'pageCount': 1}

    print 'itemList total count ' + r_server.get('itemList_counter')
    return JsonResponse(context)


def getCurrent(request):
    connection = mongo.Mongo()
    r_server = MyRedis.getServer(self=MyRedis)
    r_server.incr('getCurrent_counter')

    recieve = json.loads(request.GET.get('send'))

    # items = Instrument.objects.filter(type="1", id=recieve[u'currentId'])\
    #     .values('id', 'manufacturer__name', 'model', 'type', 'coast')
    # json_items = json.dumps(list(items), default=decimal_default)
    json_items = json.dumps(connection.getInstrumentById(recieve[u'currentId']), default=decimal_default)
    context = {'content': json_items,
                'information': 'INFOOOO'}

    print 'getCurrent total count ' + r_server.get('getCurrent_counter')
    return JsonResponse(context)


def submitPurchase(request):
    connection = mongo.Mongo()
    context = {}
    # recieve = request.GET.get('send')
    # print(recieve[u'typeId'])
    connection.updateInstrument(1, 99)
    print "PURCHASE"
    # test()
    # send_mail()
    test.delay()
    return JsonResponse(context)