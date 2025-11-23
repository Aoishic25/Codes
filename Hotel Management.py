import pandas as pd
import numpy as np


def Roomno():
    d={
        "First floor": [101,102,103,104,105,106,107,108,109,110,111,112],
        "Second floor": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212],
        "Third floor": [301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312],
        "Fourth floor": [401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412],
        "Fifth floor": [501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512],
        "Sixth floor": [601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612],
        "Seventh floor": [701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712],
        "Eighth floor": [801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812],
        "Ninth floor": [901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912],
        "Tenth floor": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012],
        "Eleventh floor": ["Meeting room"] * 12,
        "Twelfth floor": ["Meeting room"] * 12,
        "Thirteenth floor": ["Meeting room"] * 12,
        "Fourteenth floor": ["Meeting room"] * 12
    }
    df1=pd.DataFrame(d)
    df1.index+=1
    print(df1)

def Schedule():
    d1=pd.DataFrame({
        'Name':['Breakfast','Lunch','Dinner'],
        'Timings':['6:30am to 10:30am','12:00pm to 3:00pm','7:00pm to 12:00am']
    })
    d1.index+=1
    print(d1)

def Menu():
    #Breakfast
    a={
        'Breakfast':['Blueberry and banana pancakes','Organic berry waffle','Brioche French toast',
                   'Cottage cheese, fresh seasonal berries','Steak and eggs', 'NY Strip Steak',
                   'Crisp Breakfast potatoes','Idli and Sambar/Chutney','Steel-cut,brown sugar,raisins and milk',
                   'Cereal,choice of berries/sliced banana,milk','English muffin', 'Egg white frittata,smoked salmon,cream cheese,spinach,tomatoes',
                   "Goat's cheese omelet,Asparagus,spinach",'Buttermilk pancakes,whipped butter,pure maple syrup'
                   ],
        'Price1':[45,45,45,30,85,85,85,35,30,30,60,60,60,45]
    }

    #Lunch
    b={
        'Lunch':['Shrimp Cocktail','Organic Chicken Quesadilla','California rolls',
                 'Char-grilled Tiger prawns','The Famous Butter Chicken','Steak and Mushroom pie',
                 'Grilled Chicken Paillard', 'Fried Egg Noodles','Cold Mezzeh',
                 'Hot Mezzeh','Fresh Sustainable Fish,simply grilled','Malaysian Seafood Laksa',
                 'Arabic Mixed Grill','Sea bass with black quinoa,roasted baby leeks and celeriac Purée'
                 ],
        'Price2':[68, 62, 52, 62, 88, 78, 95, 72, 75, 90, 95, 72, 165, 110]
    }

    #Dinner
    c={
        'Dinner':['Rosemary rack of lamb with date Purée','Miso marinated cod,Asian vegetables and teriyaki sauce','Thai short ribs with spicy prawns',
                  'Slow-braised lamb shank', 'Wild mushroom and truffle risotto (v)','Seafood Spaghetti in garlic and white wine sauce (Alcohol)',
                  'Beetroot risotto with baby vegetables and ricotta cheese (v)', 'Black risotto with grilled cuttlefish and coriander emulsion',
                  'Chicken breast with mushroom duxelle,fingerling potatoes and sautéed brussels sprouts', 'Thai short ribs with spicy prawns,sweetcorn and shiitake mushrooms',
                  'Vegetable roll (v)','Tempura shrimp roll','Spicy tuna roll','California roll with king crab'
                  ],
        'Price3':[135, 120, 130, 115, 70, 65, 50, 50, 95, 130, 35, 45, 50, 45]
    }

    df_brek=pd.DataFrame(a)
    df_brek.index+=1
    df_lunch=pd.DataFrame(b)
    df_lunch.index+=1
    df_dinner=pd.DataFrame(c)
    df_dinner.index+=1

    print(df_brek)
    print(df_lunch)
    print(df_dinner)

    #Drinks
    d5=pd.DataFrame({
        'Drinks and Beverages':['White Wine','Rosé Wine','Sparkling Wine','Beer','Cider',
                                'Scotch Whiskey','Single Malt Whisky','Gin','Vodka','Rum',
                                'Tequila','Cognac','Aperitif and Liqueur', 'Handcrafted drinks',
                                'Soft drinks','Tea','Coffee'
        ],
        'Price': [55, 55, 55, 30, 40, 65, 70, 50, 55, 45, 60, 75, 55, 37, 25, 32, 32]
    })
    d5.index+=1
    print(d5)

def Activities():
    b={
        "Activities":['Gym','Pool','Gaming room','Bar','Free shuttle buses to selected locations','Speed boat rides'],
        "Timings":['7:00AM to 7:00pm','7:00am to 6:30pm','9:00am to 11:30pm','5:30pm to 12:00pm','6:00am to 3:00pm','8:00am to 4:30pm']
    }
    d6=pd.DataFrame(b)
    d6.index+=1
    print(d6)

def Locations():
    c={
        'Locations':['Minimart','Hair Salon','Sauna and steam room','Laundry shop',
                     'Spa','Squash,Football,Basketball and Volleyball','Souvenir,Perfume and Makeup shop'
                     ],
        'Timings':['24 hr','6:30am to 10:00pm','6:30am to 7:00pm','6:00am to 9:00pm',
                   '6:00am to 5:30pm','6:30am to 9:00pm','5:30am to 10:30pm'
                   ]
    }
    d7=pd.DataFrame(c)
    d7.index+=1
    print(d7)

a1 = input("Enter your name: ")
b1 = int(input("Enter your age: "))
d1 = input("Enter your gender: ")

if d1.lower() in ['female', 'f', 'girl', 'woman']:
    n = 'Maam'
else:
    n = 'Sir'

print(f"\nWelcome {n}!\n")

while True:
    print("\nWhat would you like to see?")
    print("Hotel Menu ---->")
    print("1: Room numbers")
    print("2: Restaurant details")
    print("3: Activities")
    print("4: Locations")
    print("5: Exit")

    c1 = int(input("Enter your choice: "))

    if c1 == 1:
        Roomno()

    elif c1 == 2:
        print("\nRestaurant Section:")
        print("1: Dining schedule")
        print("2: Full menu")
        e = int(input("Select your choice: "))

        if e == 1:
            Schedule()
        elif e == 2:
            Menu()
        else:
            print("Invalid option!")

    elif c1 == 3:
        Activities()

    elif c1 == 4:
        Locations()

    elif c1 == 5:
        print("Thank you for visiting! Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")