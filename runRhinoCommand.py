from FloorPlanInRhino3D import *

#fp = FloorPlaneInRhino3D()
name = 'CS 188'
fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75}
myFruitShop = FruitShop(name, fruitPrices)
#myFruitShop = shop.FruitShop(name, fruitPrices)
print myFruitShop.getCostPerPound('apples')