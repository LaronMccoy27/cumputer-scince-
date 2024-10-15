# create a function called free_shipping
# that tells you if you qualify for free shipping or not 
# you only get free shipping if
# you are a prime member OR order is at least $25
# you are at least 18 years old OR have parents consent 
# your functions should take four parameters
# prime (bool), cost (float), 

def free_shipping(age, consent, number):
    if age >= 19 and consent == True and number == True:
        print("BET you can have free shipping")

    else:
        print("YEAH man you aint getting free shhipping ")

free_shipping(18, True, True)