from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from .schemas import HospitalSchema
from .models import Hospital
from typing import List
from django.db import models

app = NinjaAPI(title="Hospitals API",version="1.0.0")

# Routes
# CRUD/ CRUD DUA API

@app.get("/hospitals/{hospital_id}",response=HospitalSchema)
def read_hospital(request, hospital_id: int):
    hospital = get_object_or_404(Hospital,id=hospital_id)
    return hospital


@app.get("/hospitals/",response=List[HospitalSchema])
def list_hospital(request):
    hospitals = Hospital.objects.all()
    return hospitals


# /hospitals/search/?query="nameof hospital or city"
@app.get("/hospitals/search/",response=List[HospitalSchema])
def search_hospitals(request, query: str):
    hospitals = Hospital.objects.filter(models.Q(hospital_name__icontains=query) | 
                                        models.Q(city_town__icontains=query) )
    return list(hospitals)

