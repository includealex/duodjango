from django.shortcuts import render
from django.core.cache import cache


def index(request):
    cache.clear()
    return render(request, "index.html")
