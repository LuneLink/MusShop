from django.db import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(Type, self).__init__(*args, **kwargs)


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(Manufacturer, self).__init__(*args, **kwargs)


class Size(models.Model):
    height = models.DecimalField(max_digits=4, decimal_places=2)
    width = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.height)

    def __init__(self, *args, **kwargs):
        super(Size, self).__init__(*args, **kwargs)


class Instrument(models.Model):
    count = models.IntegerField()
    # coast = models.DecimalField(max_digits=10, decimal_places=2)  # cost
    coast = models.IntegerField()
    model = models.CharField(max_length=30)
    # info

    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return self.model

    def __init__(self, *args, **kwargs):
        super(Instrument, self).__init__(*args, **kwargs)

