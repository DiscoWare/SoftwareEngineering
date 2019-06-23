from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from .models import Item, Inventory, Order, Address
from django.urls import reverse
import datetime

# Create your views here.

def homepage(request):

	# request.session.flush()


	# Setup request sessions
	# If cart/quantity does not exist since user hasn't visited, then create a new variable.
	if 'cart_id' not in request.session:
		# Note: Make a temporary cart object with placeholders
		new_cart = Order(date=datetime.datetime.now(),total_price=0,
						 delivery_address=Address.objects.all().first(),
						 delivery_choice='D')
		new_cart.save()
		request.session['cart_id'] = new_cart.id
	
	# Get the list of inventory items and separate them into pages
	item_list = Inventory.objects.all()
	paginator = Paginator(item_list, 15)
	page = request.GET.get('page')
	
	try:
		InventoryList = paginator.page(page)
	except PageNotAnInteger:
		InventoryList = paginator.page(1)
	except EmptyPage:
		InventoryList = paginator.page(paginator.num_pages)
	
	return render(request=request, 
				  template_name="homepage/home.html", # Where to find the html file
				  context={"Inventory":InventoryList}) # We can pass Tutorial objects via the name "tutorials"


def add_to_cart(request, item):
	
	# Check if web page sent a POST request. 
	if request.POST:
		inventory_item = get_object_or_404(Inventory, pk=item) # Chooses item that was passed in
		chosen_quantity = request.POST.getlist('quantities') # Get from field quantites
		chosen_quantity = int(chosen_quantity[0])
		
		# Add to request session 'cart'
		if(chosen_quantity > 0):
			
			# Retrieve cart ID and order
			# Also update quantity
			cart_id = request.session['cart_id']
			print(cart_id)
			cart = Order.objects.get(id=cart_id)
			cart.ordered_inventory.add(inventory_item)
			cart.total_price += chosen_quantity * inventory_item.price
			cart.save()
			
			success_string = "%d %s added to Cart" % (chosen_quantity,inventory_item.item)
			messages.success(request, success_string)
		
		if(chosen_quantity <= 0):
			messages.error(request, "Sorry, you can't do that")
		
		return redirect(reverse('homepage:homepage'))
	

def order_page(request):

	# Retrieve object
	cart = Order.objects.get(id=request.session['cart_id'])

	return render(request=request,
				  template_name="homepage/orders.html",
				  context={"cart":cart})

def search_page(request):
	return render(request=request,
				  template_name="homepage/search.html",
				 )

def search(request):
	if request.GET:		
		search_item = request.GET.getlist("search")
		search_string = search_item[0]
		found_items = Inventory.objects.filter(item__name__icontains=search_string)

		if found_items:
			return render(request=request, 
				  template_name="homepage/searchlist.html", # Where to find the html file
				  context={"Inventory":found_items}) 
		else:
			messages.error(request, "Item: %s not found" % search_string)
			return redirect(reverse('homepage:search'))

def cart(request):
	currentCart = Order.objects.get(id=request.session['cart_id'])
	items = currentCart.ordered_inventory.all()

	return render(request = request, 
                  template_name="homepage/cart.html",
                  context={"items":currentCart.ordered_inventory.all()})

def remove_from_cart(request, item):
	inventory_item = get_object_or_404(Inventory, pk=item)
	cart_id = request.session['cart_id']
	cart = Order.objects.get(id=cart_id)
	cart.ordered_inventory.remove(inventory_item)
	cart.total_price = 0
	cart.save()

	return redirect(reverse('homepage:cart'))

