"""WEB_PY_LAB1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from MusShop import views

router = routers.DefaultRouter()
router.register(r'instruments', views.InstrumentViewSet)
router.register(r'manufacturers', views.ManufacturerViewSet)
router.register(r'sizes', views.SizeViewSet)
router.register(r'types', views.TypeViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^itemList', views.itemList),
    url(r'^getCurrent', views.getCurrent),
    url(r'^submitPurchase', views.submitPurchase),

    # url(r'^instruments', views.InstrumentViewSet, name='instruments'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
