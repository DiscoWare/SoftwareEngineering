from django import template
import math

register = template.Library()

def get_stock(value):
	stock = math.floor(value/4)

	if(stock < 10 and stock >= 0):
		return range(value)
	elif(stock == 0):
		return range(0)
	else:
		return range(13)
	


register.filter('get_stock',get_stock)

