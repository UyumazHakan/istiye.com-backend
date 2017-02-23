_author__ = 'Hakan Uyumaz'

import json

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.db.models import Q

from ..utils import custom_redirect

from ..models import Food, OrderItem, Order


def add_cart(request):
    user = request.user
    if user.is_authenticated():

            food_id = request.POST["food"]
            food = Food.objects.get(id=food_id)
            flag = True
            if user.cart.count() and not food.menu_category.menu.restaurant == user.cart.all()[0].food.menu_category.menu.restaurant:
                return HttpResponse(json.dumps(get_cart(user)))

            for item in user.cart.all():
                if item.food == food:
                    user.cart_total_price += food.price
                    user.save()
                    item.amount += 1
                    item.save()
                    flag = False
            if flag:
                user.cart_total_price += food.price
                user.save()
                item = OrderItem(food=food)
                item.save()
                user.cart.add(item)

            return HttpResponse(json.dumps(get_cart(user)))
    else:

        return HttpResponse(json.dumps(get_cart(user)))

def remove_cart(request):
    user = request.user
    if user.is_authenticated():
        try:
            food_id = request.POST["food"]
            food = Food.objects.get(id=food_id)
            print(food)
            for item in user.cart.all():
                if item.food == food:
                    user.cart_total_price -= food.price
                    user.save()
                    item.amount -= 1
                    item.save()
                    if item.amount == 0:
                        user.cart_total_price -= food.price
                        user.save()
                        item.delete()

        finally:
            return HttpResponse(json.dumps(get_cart(user)))
    else:

        return HttpResponse(json.dumps(get_cart(user)))

def make_order(request):
    if request.user.is_authenticated():
        user = request.user
        new_order = Order(type=0,order_owner=user, restaurant = user.cart.all()[0].food.menu_category.menu.restaurant)
        new_order.save()
        for item in user.cart.all():
            new_order.items.add(item)
            new_order.save()
        new_order.total_price = user.cart_total_price
        user.cart.clear()
        user.cart_total_price = 0
        new_order.save()
        user.save()
        return custom_redirect('index', type = 1, head = "Siparisiniz Alindi", body = "Siparisiniz basariyla alinmistir, tesekkurler.")
    else:

        return redirect("index")

def get_orders(request):
    user = request.user
    if user.is_authenticated() and user.is_owner:
        orders = user.restaurant.orders.all()
        response_JSON = {"orders": []}
        for order in orders:
            orderJSON = {}
            orderJSON["id"] = order.id
            orderJSON["name"] = str(order)
            orderJSON["type_id"] = order.type
            orderJSON["total_price"] = order.total_price
            response_JSON["orders"].append(orderJSON)
        return HttpResponse(json.dumps(response_JSON))
    else:
        return HttpResponse("")

def get_active_orders(request):
        user = request.user
        if user.is_authenticated() and user.is_owner:
            orders = user.restaurant.orders.filter(~Q(type = 3))
            response_JSON = {"orders": []}
            for order in orders:
                orderJSON = {}
                orderJSON["id"] = order.id
                orderJSON["name"] = str(order)
                orderJSON["type_id"] = order.type
                orderJSON["total_price"] = order.total_price
                response_JSON["orders"].append(orderJSON)
            return HttpResponse(json.dumps(response_JSON))
        else:
            return HttpResponse("")

def get_order(request):
    user = request.user
    if user.is_authenticated() and user.is_owner:
        order_id = request.POST["order"]
        order = Order.objects.get(id=order_id)
        return HttpResponse(json.dumps(get_orderJSON(order)))
    else:
        return HttpResponse("")

def process_order(request):
    user = request.user
    if user.is_authenticated() and user.is_owner:
        order_id = request.POST["order"]
        order = Order.objects.get(id=order_id)
        order_type = order.type
        print(order_type)
        if order_type == "0":
            order.type = "1"
        elif order_type == "1":
            order.type = "2"
        elif order_type == "2":
            order.type = "3"
        print(order.type)
        order.save()
        return HttpResponse(json.dumps(get_orderJSON(order)))
    else:
        return HttpResponse("")


def get_orderJSON(order):
    responseJSON = {}
    responseJSON["id"] = order.id
    responseJSON["type"] = order.get_type_display()
    responseJSON["type_id"] = order.type
    responseJSON["order_owner"] = str(order.order_owner)
    responseJSON["is_active"] = order.is_active
    responseJSON["date"] = str(order.date)
    responseJSON["total_price"] = order.total_price
    responseJSON["restaurant"] = str(order.restaurant)
    responseJSON["items"] = []
    for item in order.items.all():
        itemJSON = {}
        itemJSON["amount"] = item.amount
        itemJSON["name"] = item.food.name
        itemJSON["food_id"] = item.food.id
        responseJSON["items"].append(itemJSON)
    return responseJSON


def get_cart(user):
    responseJSON = {}
    responseJSON["total_price"] = user.cart_total_price
    responseJSON["items"] = []
    for item in user.cart.all():
        itemJSON = {}
        itemJSON["amount"] = item.amount
        itemJSON["name"] = item.food.name
        itemJSON["food_id"] = item.food.id
        responseJSON["items"].append(itemJSON)
    return responseJSON



