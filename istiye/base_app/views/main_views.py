__author__ = 'Hakan Uyumaz'

from django.shortcuts import render, redirect
from django.db.models import Q

from ..models import Restaurant, Food




def index_view(request):
    if "type" in request.GET:
        message = {}
        message["type"] = request.GET["type"]
        message["head"] = request.GET["head"]
        message["body"] = request.GET["body"]
        print(message)
        return render(request, "index.html", {"message": message})
    return render(request, "index.html")


def search_view(request):
    if request.method != "POST" or not "key" in request.POST:
        return redirect("index")
    key = request.POST["key"]
    restaurants_with_key = Restaurant.objects.filter(Q(name__icontains=key) | Q(type__icontains=key))
    foods_with_key = Food.objects.filter(Q(name__icontains=key))
    restaurants = []
    for restaurant in restaurants_with_key:
        restaurants.append(restaurant)
    for food in foods_with_key:
        restaurants.append(food.menu_category.menu.restaurant)
    restaurants = list(set(restaurants))
    return render(request, "restaurants.html", {"restaurants": restaurants})


def restaurants_view(request):
    if request.user.is_authenticated():
        user = request.user
        restaurants = Restaurant.objects.all()
        return render(request, "restaurants.html",
                      {"restaurants": restaurants})
    else:
        return redirect("index")
