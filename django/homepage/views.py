from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Item, Inventory

# Create your views here.

def homepage(request):
	# if request.method == 'POST':
			#do something
	item_list = Inventory.objects.all()
	paginator = Paginator(item_list, 25)
	page = request.GET.get('page')
	Inventorya = paginator.get_page(page)
	
	return render(request=request, 
				  template_name="homepage/home.html", # Where to find the html file
				  context={"Inventory":Inventorya}) # We can pass Tutorial objects via the name "tutorials"
