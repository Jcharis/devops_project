from django.db import models

# Create your models here.
class Hospital(models.Model):
    facility_bed = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255,blank=True,null=True)
    hospital_name = models.CharField(max_length=255,blank=True,null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    city_town = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.hospital_name