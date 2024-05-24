from django.urls import path
from . import views
from .api import app 

urlpatterns = [
    path("", views.index, name="home"),

    # API
    path("api/", app.urls),
   
]