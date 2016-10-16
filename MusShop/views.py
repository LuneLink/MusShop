import json
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
    items = Instrument.objects.filter(type="1").values('id', 'manufacturer__name', 'model', 'type')
    print("Items: ")
    print(items)
    # posts = (Post.objects.filter(owner=authenticated_user)
    #
    #         .values('id', 'title', 'summary'))
    json_items = json.dumps(list(items))
    print("JSON Items: ")
    print(json_items)

    search = json.loads(request.GET.get('send'))[u'searchParams']
    print("Search")
    print(search)
    context = {'content': json_items,
               'pageCount': 1}
    # if(search == {}):
    #     context = {'message': "GET OUT!",
    #                'pageCount': 2,
    #                'content': [
    #                {
    #                     'id': 1,
    #                     'manufacturer__name': 'Jackson',
    #                     'model': 'KingV',
    #                     'cost': 100
    #                },
    #                {
    #                    'id': 2,
    #                    'manufacturer__name': 'Jackson',
    #                    'model': 'Dinky DK2',
    #                    'cost': 100
    #                },
    #                {
    #                    'id': 3,
    #                    'manufacturer__name': 'Jackson',
    #                    'model': 'Dinky DK7-M',
    #                    'cost': 100
    #                },
    #                {
    #                    'id': 4,
    #                    'manufacturer__name': 'Jackson',
    #                    'model': 'Minion',
    #                    'cost': 100
    #                }
    #            ]}
    # else:
    #     context = {'message': "GET OUT!",
    #                'pageCount': 1,
    #                'content': [
    #                    {
    #                        'id': 1,
    #                        'manufacturer__name': 'Jackson',
    #                        'model': 'KingV',
    #                        'cost': 100
    #                    },
    #                    {
    #                        'id': 1,
    #                        'manufacturer__name': 'Jackson',
    #                        'model': 'KingV',
    #                        'cost': 100
    #                    },
    #                    {
    #                        'id': 3,
    #                        'manufacturer__name': 'Jackson',
    #                        'model': 'Dinky DK7-M',
    #                        'cost': 100
    #                    },
    #                    {
    #                        'id': 4,
    #                        'manufacturer__name': 'Jackson',
    #                        'model': 'Minion',
    #                        'cost': 100
    #                    }
    #                ]}

    print(request.GET.get('send'))
    return JsonResponse(context)
    # return render(request, "test.html", context)


def getCurrent(request):
    recieve = json.loads(request.GET.get('send'))
    print(recieve[u'typeId'])
    print(recieve[u'currentId'])

    items = Instrument.objects.filter(type="1", id=recieve[u'currentId']).values('id', 'manufacturer__name', 'model', 'type')
    json_items = json.dumps(list(items))
    context = {'content': json_items,
                'information': 'INFOOOO',
               'cost': 100}
    # context = {'information': 'Some awesome information',
    #            #'id': int(request.GET.get('send')[u'currentId']),
    #            'cost': 100,
    #            'manufacturer': 'Jackson',
    #            'model': 'KingV'}



    return JsonResponse(context)


def submitPurchase(request):
    context = {}
    # recieve = request.GET.get('send')
    # print(recieve[u'typeId'])

    return JsonResponse(context)
