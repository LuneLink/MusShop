from models import Instrument, Manufacturer, Size, Type
from rest_framework import serializers


class InstrumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instrument
        fields = ('count', 'coast', 'model', 'type', 'manufacturer', 'size')


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name')


class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = ('height', 'width')


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('name')

