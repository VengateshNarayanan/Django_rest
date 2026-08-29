from django.db import models

# Create your models here.

class Turf(models.Model):
    booking_ref = models.CharField(max_length=20,blank=True)
    customer_name = models.CharField(max_length=20,blank=True)
    turf_name = models.CharField(max_length=20 , blank=True)
    sport_name = models.CharField(max_length=20 , blank=True)
    booking_datetime = models.DateTimeField(max_length=20)
    total_amount = models.IntegerField(max_length=20)
