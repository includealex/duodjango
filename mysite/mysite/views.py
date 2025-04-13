from django.shortcuts import render
from django.core.cache import cache
from . import analogues_manager

def index(request):
    return render(request, "index.html")

def get_analogues(request):
    analogues = analogues_manager.get_current_analogues()
    return render(request, "analogues.html", context={"analogues": analogues})
