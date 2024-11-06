#python has four types of collections 
#tuple
#set
#>list
#>dictionary

#today, were going to focus on listssstssttstsss
# a list is a way to store more than one value in single variable 
#items can be access by their index(posititon in the list) indinces

best_elden_weapons = ["blashhemous blade", "moonveil", "river of blood", "iron ball", "bloodhound's fang"]
best_years = [1776, 1985, 1994, 1957, 2016]
myint = 3

print(len(best_elden_rint_weapon))




print(best_years[0])                     #print the first item
print(best_elden_rint_weapon[4])         #print the last item
print(best_elden_ring_weapon[len(best_elden_ring_weapon)-1])



import random
def drop_item():
    roll = random.randint(0,10000)
    if roll < 7000:
        print("NORMAL ITEM")

    elif roll < 9000:
        print("MAGIC ITEM")
        
    elif roll < 9900:
        print("RARE ITEM")
        
    elif roll < 9990:
        print("LEGENDARY ITEM")
        
    elif roll <= 10000:
        print("UBER ITEM")

    if input("Play again?\n>") == "y":
        drop_item()

drop_item()












