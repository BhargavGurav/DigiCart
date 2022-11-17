from django.contrib import admin
from .models import AddMobile, AddLaptop, AddMenItem, AddWomenItem, AddKidsItem, AddHomeItem, AddGrocery, AddWatche, AddFootwear, Customer, Cart, History
# Register your models here.
admin.site.site_header = 'DigiCart | Administration'

admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(History)
admin.site.register(AddMobile)
admin.site.register(AddLaptop)
admin.site.register(AddMenItem)
admin.site.register(AddWomenItem)
admin.site.register(AddKidsItem)
admin.site.register(AddHomeItem)
admin.site.register(AddGrocery)
admin.site.register(AddWatche)
admin.site.register(AddFootwear)

