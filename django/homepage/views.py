from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial,Item

# Create your views here.

def homepage(request):
	# if request.method == 'POST':
			#do something
	return render(request=request, 
				  template_name="homepage/home.html", # Where to find the html file
				  context={"tutorials": Tutorial.objects.all,"Items":Item.objects.all}) # We can pass Tutorial objects via the name "tutorials"
