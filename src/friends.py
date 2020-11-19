def get_name(person):
    return person ["name"]


def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]


def likes_to_eat(person,food):
    snacks = person["favourites"]["snacks"]
    for snack in snacks:
        if snack == food:
            return True
    return False 

#return food in person["favourites"]["snacks"]

def add_friend(person,friend):
    friends = person["friends"]
    friends.append(friend)

#person["friends"].append(friend)

def remove_friend(person,friend):
    friends = person["friends"]
    friends.remove(friend)

def total_money(people):
    stolen_monies = 0
    for person in people:
        stolen_monies += person["monies"]
    return stolen_monies

def l_money(lender, lendee, amount):
    lenders_money = lender["monies"]
    #if lenders_money < amount:
    #    print("Not enough money, go somewhere else!")
    lendees_money = lendee["monies"]
    lenders_money -= amount
    lendees_money += amount
   

    