# exception handling    
# write a program that asks for two numbers and divides them 


# if   =   try
# else   =    except
def divide_two_number():
    try:      # we always enter the try block, there is no condition 
        x = int(input("what is the first number?\n>"))
        y = int(input("what is the second number?\n>"))
        print(x / y)



        except:  # if anything in the try block causes an error,
                 # the try block stops immditately and the except is ran instead
                 # the rest of the try block never finisher running, its skipped 
                 # if the try block executes without an error,  the except is skipped 
                # the only way to get into the except is to "throw" an error 
            print("IDk what you did, but you broke it .. try again")
            divide_two_number()     # tell the function to run again 