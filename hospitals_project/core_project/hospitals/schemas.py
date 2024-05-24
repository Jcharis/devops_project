from ninja import  ModelSchema
from .models import Hospital

# Similar ModelSerializer from DRF
class HospitalSchema(ModelSchema):
   
    class Meta:
        model = Hospital
        fields = ["facility_bed","district", "hospital_name","website","city_town"]
        