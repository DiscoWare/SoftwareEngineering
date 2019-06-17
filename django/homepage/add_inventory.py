from homepage.models import Item, Inventory, GroceryStore 
import random 

def get_random(modelName):
    return modelName.objects.order_by("?").first()

for x in range(0,50):
	curr_item = get_random(Item)
	grocery_item = curr_item.name;
	random_price = random.randint(99,2400)/100
	random_quant = random.randint(0,301)
	gstore = get_random(GroceryStore)
	new_inventory = Inventory(item=curr_item,price=random_price,
							  stock=random_quant,store=gstore)
	new_inventory.save()



print("Success")