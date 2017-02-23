_author__ = 'Hakan Uyumaz'

import json

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q

from ..models import Restaurant, Menu, Menu_Category, Food

def restaurant(request, restaurant_id):
    if request.user.is_authenticated():
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
        except Restaurant.DoesNotExist:
            return redirect("index")
        return render(request, "restaurant.html",
                      {"user": request.user, "restaurant": restaurant})
    else:
        return redirect("index")

def order_list(request):
    user = request.user
    if user.is_authenticated() and user.is_owner:
        restaurant = user.restaurant
        orders = restaurant.orders.filter(~Q(type=3))

        return render(request, "orders.html", {"orders": orders})
    else:
        return redirect("index")

def get_food(request):
    user = request.user
    if user.is_authenticated() and user.is_owner:
        food_id = request.POST["food"]
        food = Food.objects.get(id=food_id)
        return HttpResponse(json.dumps(get_foodJSON(food)))
    else:
        return HttpResponse("")

def get_foodJSON(food):
    responseJSON = {}
    responseJSON["id"] = food.id
    responseJSON["price"] = food.price
    if food.photo:
        responseJSON["img"] = food.photo.url
    responseJSON["description"] = food.description
    return responseJSON