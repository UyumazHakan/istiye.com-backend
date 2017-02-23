"""istiye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.contrib import admin
from base_app.admin import admin_site

import base_app.views.main_views as main
import base_app.views.user_views as user
import base_app.views.restaurant_views as restaurant
import base_app.views.order_views as order

urlpatterns = [
    url(r'^admin/', admin_site.urls),
    url(r'^$', main.index_view, name='index'),
    url(r'^search/$', main.search_view, name='search'),
    url(r'^register/$', user.register_user, name='register'),
    url(r'^edit_profile/$', user.edit_profile, name='edit_profile'),
    url(r'^login/$', user.login_user, name='login'),
    url(r'^logout/$', user.logout_user, name='logout'),
    url(r'^add_cart/$', order.add_cart, name='add_cart'),
    url(r'^remove_cart/$', order.remove_cart, name='remove_cart'),
    url(r'^make_order/$', order.make_order, name='make_order'),
    url(r'^restaurants/$', main.restaurants_view, name='restaurants'),
    url(r'^restaurant/(?P<restaurant_id>[^/]+)/$', restaurant.restaurant, name='restaurant'),
    url(r'^orders/$', restaurant.order_list, name='orders'),
    url(r'^get_active_orders/$', order.get_active_orders, name='activeOrdersJSON'),
    url(r'^get_orders/$', order.get_orders, name='ordersJSON'),
    url(r'^get_order/$', order.get_order, name='orderJSON'),
    url(r'^get_food/$', restaurant.get_food, name='foodJSON'),
    url(r'^process_order/$', order.process_order, name='process_order')


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)