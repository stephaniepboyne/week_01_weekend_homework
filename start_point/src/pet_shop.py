def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"] 

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, num):
    cc_pet_shop["admin"]["total_cash"] += num  

def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

def increase_pets_sold(cc_pet_shop, num):
    cc_pet_shop["admin"]["pets_sold"] += num 

def get_stock_count(cc_pet_shop):
    return len(cc_pet_shop["pets"])

def get_pets_by_breed(cc_pet_shop, breed):
    num_of_pets = [] 
    for pet in cc_pet_shop["pets"]:
        if pet["breed"] == breed:
            num_of_pets.append(pet)
    return num_of_pets
  
def find_pet_by_name(cc_pet_shop, name):
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(cc_pet_shop, name):       
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == name:
            cc_pet_shop["pets"].remove(pet)

def add_pet_to_stock(cc_pet_shop, new_pet): 
    cc_pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, num):
    customers["cash"] -= num

def get_customer_pet_count(customers):
    customer_pet_count = len(customers["pets"])
    return customer_pet_count

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    can_buy_pet = True
    if customer["cash"] >= new_pet["price"]:
        can_buy_pet
    else:
        can_buy_pet = False 
    return can_buy_pet

def sell_pet_to_customer(cc_pet_shop, pet, customer):
    for animal in cc_pet_shop["pets"]:
        if animal == pet:
            if customer["cash"] >= pet["price"]:
                customer["pets"].append(pet) 
                cc_pet_shop["admin"]["pets_sold"] += 1 
                customer["cash"] -= pet["price"]
                cc_pet_shop["admin"]["total_cash"] += pet["price"]