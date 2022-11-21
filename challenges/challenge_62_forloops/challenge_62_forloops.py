#!/usr/bin/env python3
farms1 = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

fresh = ["carrots", "celery", "bananas", "apples", "oranges"]

def allAnimals(farm):
    for animals in farms[farm]["agriculture"]:
        if animals not in fresh:
            print(animals)

def allFarms():
    farmList = []

    for farm in farms:
        farmList.append(farm["name"])
    farmString = ', '.join(map(str,farmList))

    return farmString

def userFarm():
    farmChoices = allFarms()
    userChoice = input(f"Choose a farm: {farmChoices}\n>")    

    return optionConversion(userChoice)

def optionConversion(farmChoice):
    choice = 0
    iteration = 0
    validChoice = False

    for farm in farms:
        if farmChoice.lower() == farm["name"].lower():
            choice = iteration
            validChoice = True
        iteration += 1

    if validChoice == False:
        choice = userFarm()
    return choice

def main():
    allAnimals(userFarm())

if __name__ == "__main__":
    main()
