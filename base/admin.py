from django.contrib import admin

from .models import Clients, Goods, OrderInfo, Orders, Pay, Staff, Suppliers

admin.site.register(Clients)
admin.site.register(Goods)
admin.site.register(OrderInfo)
admin.site.register(Orders)
admin.site.register(Pay)
admin.site.register(Staff)
