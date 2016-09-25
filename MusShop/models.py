from django.db import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Size(models.Model):
    height = models.DecimalField(max_digits=4, decimal_places=2)
    width = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.height


class Instrument(models.Model):
    count = models.IntegerField()
    coast = models.DecimalField(max_digits=10, decimal_places=2)  # cost
    model = models.CharField(max_length=30)
    # info

    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return self.model
