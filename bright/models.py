from django.db import models


# Create your models here.
class Members(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_of_birth = models.DateField(blank=True, null=True)
    staff_team = models.CharField(max_length=20, blank=True)
    staff_rank = models.IntegerField(blank=True, null=True)
