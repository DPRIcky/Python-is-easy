myUniqueList = []  # Creating an empty list
myLeftovers = []   # Creating an empty list

# Defining a function to check if an element is already in "MY UNIQUE LIST" or not #

def add(element):
    if element not in myUniqueList:
        myUniqueList.append(element)            # If the element is not in "My Unique List" it adds the element #
        print(myUniqueList)
        print(True)
    else:
        myLeftovers.append(element)             # If the element already exist in "My Unique List" it adds the element to "My Leftovers" #     
        print(myLeftovers)
        print(False)

add(5)
add(7)
add(9)
add(5)
add(12)
add(9)
add(7)