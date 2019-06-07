from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Tutorial,Item

# Create your views here.

def homepage(request):
	# if request.method == 'POST':
			#do something
	item_list = Item.objects.all();
	paginator = Paginator(item_list, 1)
	page = request.GET.get('page')
	Items = paginator.get_page(page)

	return render(request=request, 
				  template_name="homepage/home.html", # Where to find the html file
				  context={"tutorials": Tutorial.objects.all,"Items":Items}) # We can pass Tutorial objects via the name "tutorials"
