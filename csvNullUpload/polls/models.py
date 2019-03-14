from django.db import models
from django.db.models import DurationField
import datetime

# Create your models here.

#class camtelclient(models.Model):
#    Date = models.DateTimeField()
#    Inbound = models.CharField(max_length=30)
#    col2_cdefa = models.CharField(max_length=30)
#    Outbound = models.CharField(max_length=30)
#    col4_cdeff = models.CharField(max_length=30)
#    col5_cdefa = models.CharField(max_length=30)
#    col6_cdefbb = models.CharField(max_length=30)

    #def __str__(self):
    #	return "{0} {1} {3}".format(self.Date, self.Inbound, self.Outbound)

class output(models.Model):
	Number = models.IntegerField(null=True, blank=True)
	DateDeCoupure = models.DateTimeField(null=True, blank=True)
	DateDeRetablisement = models.DateTimeField(null=True, blank=True)
	Duree = DurationField(null=True, blank=True)
	client = models.TextField(null=True, blank=True)
	camtel = models.TextField(null=True, blank=True)
	observation = models.TextField(null=True, blank=True)
	def __str__(self):
		return f"{self.Number} {self.DateDeCoupure} {self.DateDeRetablisement} {self.Duree}"

class title(models.Model):
	Title = models.CharField(max_length=100)		
