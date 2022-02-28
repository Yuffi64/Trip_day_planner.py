import random


location = ["Canada", "Germany", "New Zealand", "Japan", "Italy", "Bora Bora"]
transport = ["a car", "a train", "a plane", "the bus", "teleportation", "a magic carpet", "a pirate Ship"]
food = ["Culture food in the area", "tacos", "pizza", "sea food", "steaks"]
entertainment = ["Casinos", "Aquarium", "Zoo", "National Park", "Bleach", "Historical Museum", "Art Gallery"]



def location_gen(location_lists):
    print("Welcome to the Amazing day trip planner! Where all of your I don't know what to do today becomes a spontaneous Adventure!")
    location_rand = random.choice(location_lists)
    first_question = input(f'Lets start off with {location_rand}, does that sound like a good start? Please select y/n: ') 
    while first_question == "n":
        location_rand = random.choice(location_lists)
        first_question = input(f'Ops! that was not a good place anyways. Well how does {location_rand} sound? Select y/n: ')
    if first_question == "y":
        print("Awesome! But... Any thoughts on how are you going to get there? That's ok!")
    return location_rand


def transport_gen(transport_lists):
    transport_rand = random.choice(transport_lists)
    second_question = input(f'We have selected {transport_rand} for your sweet ride! Does this sound good? select y/n: ')
    while second_question == 'n':
        transport_rand = random.choice(transport_lists)
        second_question = input(f"That's okay, not everyone likes that method of transport. But no worries! There is always {transport_rand}! How does that sound? select y/n: ")
    if second_question == 'y':
            print("Awesome sauce! Um... I am not sure about you but food on this trip would be pretty great don't you think?")
    return transport_rand


def food_gen(food_lists):
    food_rand = random.choice(food_lists)
    third_question = input(f"We have selected {food_rand} for a place you should try to eat, what do you think? select y/n: ")
    while third_question == "n": 
        food_rand = random.choice(food_lists)
        third_question = input(f"Darn, I was sure that would hit the stop. That's okay we have something else, how does {food_rand} sound? Select y/n: ")
    if third_question == "y": 
         print("AHH YEE! We are almost done!")
    return food_rand

def entertainment_gen(entertainment_lists):
    entertainment_rand = random.choice(entertainment_lists)
    fourth_question = input(f'The soul purpose of this day is to not make it boring. A fun think to do is check out the {entertainment_rand} for your entertainment! Does this sound fun? select y/n: ')
    while fourth_question == 'n':
        entertainment_rand = random.choice(entertainment_lists)
        fourth_question = input(f"Well shoot, we were sure that would had worked, But thats ok! we have decided the {entertainment_rand} would be a great spot to check out. What do you think? select y/n: ")
    if fourth_question == 'y':
        print("YAY! We did it! Now lets go over what we had decided of your awesome adventure!")
    return entertainment_rand

location_rand = location_gen(location)
transport_rand = transport_gen(transport)
food_rand = food_gen(food)
entertainment_rand = entertainment_gen(entertainment)

def last_step(final_decision):
    final = final_decision
    print(f'Location is: {location_rand}')
    print(f'Form of arrival is: {transport_rand}')
    print(f'Type of food will be: {food_rand}')
    print(f'Fun adventure will be: {entertainment_rand}')
    
    last_question = input("Does this sounds like an adventure? y/n: ")
    while last_question == 'n':
        last_question = input('Well We guess we can do this all over again.')
    if last_question == 'y':
        print(f"This was fun! Now go and get ready to see {location_rand} by {transport_rand} where you can stuff your face with some {food_rand} and enjoy the day at the {entertainment_rand}. Come back again!")
        return  

final = last_step("")