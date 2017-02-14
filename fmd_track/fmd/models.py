from django.db import models


class Farm(models.Model):
    farm_id = models.IntegerField()
    name = models.CharField(max_length=300)
    address = models.TextField()


class FmdData(models.Model):
    name = models.CharField(max_length=300)
    fmd = models.ForeignKey(Farm)

    date_observed = models.DateField()
    time_observed = models.TimeField()

    farm_condition = models.TextField()
    bgp_requirements = models.TextField()
    corrective_action = models.TextField()

    hand_delivered_date = models.DateField()
    hand_delivered_time = models.TimeField()

    corrected_date = models.DateField()
    corrected_time = models.TimeField()
