from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"page_title": "Hospitals"}
    return render(request, "index.html",context)
