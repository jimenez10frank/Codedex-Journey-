class Restaurant:
    name = ""
    category = ""
    rating = 0.0
    delivery = True

bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False
print(vars(bobs_burgers))
mcDonalds = Restaurant()
mcDonalds.name = 'mcDoablds'
mcDonalds.category = 'American Diner'
mcDonalds.rating = 5.0
mcDonalds.delivery = True
print(vars(mcDonalds))
kfc = Restaurant()
kfc.name = 'kentucky Fried Chicken'
kfc.category = 'American Diner'
kfc.rating = 4.9
kfc.delivery = True
print(vars(kfc))