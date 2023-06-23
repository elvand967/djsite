from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.

def index(request):
    return HttpResponse("Страница приложения women.")


def categories(request, catid):
    if request.GET:
        print(request.GET)
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям.</h1><p>{catid}</p>")


def archive(request, year):
    if int(year)>2023:
        #raise Http404()
        #return redirect('/') # 302 - страница перемещена временно на другой URL-адрес
        return redirect('home', permanent=False) # 301 - страница перемещена на другой постоянный URL-адрес

    return HttpResponse(f"<h1>Архив по годам.</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена.</h1>")