from django.db import models


#class Country(models.Model):
#    country_name = models.CharField(max_length=50)
#    #country = models.ForeignKey(Country,on_delete=models.CASCADE)


class City(models.Model):
    city_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    #country_name = models.CharField(max_length=50, blank=True, null=True)


def __str__(self):
    return self.city_name