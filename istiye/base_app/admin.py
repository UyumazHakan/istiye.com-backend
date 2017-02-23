__author__ = 'Hakan Uyumaz'

from django.contrib import admin

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

from .models import User, Food, Menu, Menu_Category, Restaurant, Order, OrderItem



class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('ISTIYE')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('ISTIYE')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('ISTIYE')

admin_site = MyAdminSite()

class UserAdmin(admin.ModelAdmin):
    pass

class FoodAdmin(admin.ModelAdmin):
    pass

class MenuAdmin(admin.ModelAdmin):
    pass

class Menu_CategoryAdmin(admin.ModelAdmin):
    pass

class RestaurantAdmin(admin.ModelAdmin):
    pass

class OrderAdmin(admin.ModelAdmin):
    pass

class OrderItemAdmin(admin.ModelAdmin):
    pass


admin_site.register(User, UserAdmin)
admin_site.register(Food, FoodAdmin)
admin_site.register(Menu, MenuAdmin)
admin_site.register(Menu_Category, Menu_CategoryAdmin)
admin_site.register(Restaurant, RestaurantAdmin)
admin_site.register(Order, OrderAdmin)
admin_site.register(OrderItem, OrderItemAdmin)

