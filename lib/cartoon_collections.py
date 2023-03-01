cheese = ["cheddar", "gouda", "camembert"]

def roll_call_dwarves(list):
    index = 1 
    for name in list:
        print(f'{index}. {name}')
        index += 1

def summon_captain_planet(planeteer_calls):
   return [f'{element.title()}!' for element in planeteer_calls]
    #new_list = [f'{element.title()} "!" for element in planeteer_calls']
    #print(new_list)

def long_planeteer_calls(calls):
    for element in calls:
        if len(element) > 4:
            return True 
    return False 

def find_the_cheese(list_of_strings):
    for string in list_of_strings:
        if string in cheese:
            return string 
    return None


