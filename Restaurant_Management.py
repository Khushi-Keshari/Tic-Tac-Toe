# Menu of Dishes
menu={
    "Sandwitch": 40,
    "Pizza": 100,
    "Burger": 80,
    "Pasta": 120,
    "Coffee": 20,
    "Tea": 15
}

bill=0
print("Welcome!")
print("Have a look on menu....")
print("Sandwitch:Rs 40","\nPizza:Rs 100","\nBurger:Rs 80","\nPasta:Rs 120", "\nCoffee:Rs 20", "\nTea: Rs 50")
order="Yes"
while order=="Yes":
    item=input("What do you want to order? ")
    if item in menu:
        bill+=menu[item]
        print("This is item is added in your oder list")
    else:
        print("Sorry this item is unavilable in this Restaurant:(")
    order=input("Do you want to order more?(Yes/No) ")
print("Here is your bill->",bill)