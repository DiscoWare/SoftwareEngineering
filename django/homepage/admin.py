from django.contrib import admin
from .models import Item
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
	fields = ['item_name','item_price',
			  'store1_quant','store2_quant',
			  'store3_quant','store4_quant']

admin.site.register(Item,ItemAdmin)
