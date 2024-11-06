import random                                                                                                                                    

def start_adventure():
    print("you stand at the entrance of the a dark store. Do you:")
    print("1. do you enter")
    print("2. leave and go home")

    choice = input (">")

    if choice == "1":
        enter_store()
    elif choice =="2":
        go_home()
    else:
        print("enter dark mall")
        start_adventure()


def enter_store():
     print("you step in a store and you hear something")
     print("1. go home")
     print("2. follow the sound")
     choice = input(">")
     if choice == "1":
          go_home()
     elif choice =="2":
          follow_sound()
          
     else:print("you die")
             

def follow_sound():
     print("you follow sound and don't see anything") 
     print("you start to think if it's someone else in there with you")
     print("since your in a store you start looking for foodand you hear the same sound")
     print("1. dont mind it and keep looking for food")
     print("2. look for a weapon just incase you need one")
     choice = input(">")
     if choice == "1":
          dont_mind()

     elif choice =="2":
          look_weapon()
          
     elif choice == "3":
          you_die()


start_adventure()


def go_home():
     print("you go home because you were scared of the sounds you were hearing in the store")
     print("you never found out what you was hearing")

def dont_mind():
     print("you find a bag of chips but you never really like that bag")
     print("1.still eat them")
     print("2. leave them alone and keep serching for another bag")
     choice = input(">")
     if choice =="1":
          eat_them()

     elif choice =="2":
          leave_them()

     

def eat_them():
     print("you eat them and you dead")
     print("restart adventure")






def leave_them():
     print("drop that bag and as you do that you see something in the next aisle")
     print("1. run away to a different store")
     print("2. find a weapon so you can defend yourself")
     choice = input(">")
     if choice =="1":
          run_away()

     elif choice =="2":
          find_weapon()



def find_weapon():
     print("you go looking for a weapon")
     print("you dont find one")
     print("but you see a glowing drink on the top shelf")
     print("walk up to the shelf to grab the drink")
     print("you grab it and start drinking it and as your drinking it you feel something behide you")
     print("you look behide you and see a 10foot human eating gaint. You try running but it grabs you")
     win_chance = random.random()
     if win_chance <= .0001:
          print("you feel a boost in your blood stream. So you break free and grab a knife from his backpack")
          print("the gaint attack but you ducks it and cut the gaint finger off")
     if win_chance <= .50: 
          print("the gaint finger hit the ground it make the gaint even more mad")
          print("the gaint rush at you and you have to options")
          print("1. end him off and gain a point")
          choice = input(">")
          if choice == "1": 
               end_him()

          elif choice =="2":
               you_die()
          
          
          
          
def run_away():
     print(" you run away and try to find more drinks to gain more powers")




def end_him():
     print("the gaint runs up and you double jump and cut his head off")
     print("you have gained +1 point")
           



def different_store():
     print("you decide to go to a different store,but that adventure ends here.")



def enter_store2():
     print("you walk the store and see your favorite snacks and food")
     print("you start going to work with all your favorite foods")
     print("you see the same master that you killed in the other store")
     print("1. do you hide")
     print("2. do you keep eating")
     choice = input (">")
     if choice =="1":
          you_hide()


     elif choice == "2":
          keep_eating()


