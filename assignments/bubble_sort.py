number = [34, 7, 23, 32, 5, 62]
#print the list before it started 
#define the function
def bubble_sort(n):
    steps = 0
    #interate through every item on the list
    for j in (len(n)-1):
        for i in range(0, (len(n))-1):
        #check if the current list item is greater than the next list item
            if n[i] > n[i + 1]:
                n[i] == n[i + 1]
                n[i], n[i + 1] == n[i + 1], n[i]
                steps += 1


            #swap their vaules
            n[i], n[i+1] = n[i+1], n[i]
            print(n)
            print("Bubble Sort Steps:", str(steps))

bubble_sort(number)