from tkinter import X


Food_prices = {
    "Chicken" : "1.59", 
    "Beef" : "1.99", 
    "Cheese" : "1.00", 
    "Milk" : "2.50"
}
 
               
Consoles = {
    "Ps5" : "1000",
    "Ps4" : "300",
    "Xbox one" : "350",
    "Xbox X" : "600"
}

Ps5_prices = Consoles["Ps5"]
Ps4_prices = Consoles["Ps4"]
Xbox_one_prices = Consoles["Xbox one"]
print(Consoles ["Ps5"])

shoe_inventory = {
    "Jordan 13": 1, 
    "Yeezy": 8,
    "Foamposite": 10,
    "Air Max": 5,
    "SB Dunk": 20,

}
#costumer purchase 2 pairs of SB Dunks and Came to return a pair of Yeezy
shoe_inventory["SB Dunk"] -= 2
shoe_inventory["Yeezy"] += 1
print(shoe_inventory)

#shoes inventory Increases by 7
shoe_inventory["Jordan 13"] *= 7
shoe_inventory["Yeezy"] *= 7
shoe_inventory["Foamposite"] *=7
shoe_inventory["Air Max"] *= 7
shoe_inventory["SB Dunk"] *= 7
print(shoe_inventory)

#shoes inventory decreases decreases by 3
shoe_inventory["Jordan 13"] -= 3
shoe_inventory["Yeezy"] -= 3
shoe_inventory["Foamposite"] -= 3
shoe_inventory["Air Max"] -= 3
shoe_inventory["SB Dunk"] -= 3
print(shoe_inventory)

#adding new shoes 

shoe_inventory["Nike"] = 3
shoe_inventory["Vans"] = 2
shoe_inventory["Aldo"] = 1
print(shoe_inventory) 

#delete keys from a dictionary
del shoe_inventory["Nike"]
del shoe_inventory["Jordan 13"]
print(shoe_inventory)
