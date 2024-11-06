# nested if statements 



prime = True
cost = 20
age = 17
consent = False

# if (prime == True ot cost >=  25) and (age >= 18 or consent == True):

if prime:
    if age >= 18:
        print("FREE SHIPPING APPLIED")
    elif consent: 
        print("FREE SHIPPING APPLIED")
    else:
        print("No free ship for u...")

else:
    print("no free ship for u...")



    # decide if we need an umbrella 
    # you need an umbrella if its raining AND you are going outside that day 



raining = input("is it raining outside?\n>")
outside = input("do you plan on going ourside?\n>")

if raining.lower() == "yes":
    if outside.lower("yes"):
        print("BRING AN UMBRELLA")
    else:
        print("NO UMBRELLA")
        
else:
    print("NO UMBRELLA")        