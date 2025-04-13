from django.shortcuts import render
from django.core.cache import cache
from . import analogues_manager

def index(request):
    return render(request, "index.html")

def get_analogues(request):
    analogues = analogues_manager.get_current_analogues()
    return render(request, "analogues.html", context={"analogues": analogues})

def get_statistics(request):
    stats = analogues_manager.get_stats()
    return render(request, "statistics.html", context={"statistics": stats})

def add_analogue(request):
    return render(request, "add_analogue.html")

def send_analogue(request):
    cache.clear()
    if request.method != "POST":
        add_analogue(request)
        return

    cur_name = request.POST.get("name")
    if (len(cur_name) == 0):
        cur_name = "аноним"

    context = {"user": cur_name, "correct_input": True, "comment": ""}

    russian_word = request.POST.get("russian_word")
    if (len(russian_word) == 0):
        context["correct_input"] = False
        context["comment"] += "Русское слово должно быть введено. "

    oldrussian_word = request.POST.get("oldrussian_word")
    if (len(oldrussian_word) == 0):
        context["correct_input"] = False
        context["comment"] += "Древнерусский аналог должен быть введён. "
    
    if context["correct_input"]:
        analogues_manager.add_analogue(russian_word, oldrussian_word, cur_name)

    return render(request, "analogue_request.html", context)