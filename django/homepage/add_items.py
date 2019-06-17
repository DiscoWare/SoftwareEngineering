import json 
from homepage.models import Item

with open('./homepage/MOCK_DATA.json') as json_file:
	data = json.load(json_file)
	for item in data:
		items = Item(name=item['Item_name'],description=item['Description'])
		items.save()


print("Success")