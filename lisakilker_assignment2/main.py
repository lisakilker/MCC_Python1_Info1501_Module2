#Main class
#Imports the other classes
from rug import Rug
from carpet import Carpet

def main():
    #Create an even number of Rug objects
    rugs = [
        Rug(15, 13, 100),
        Rug(14, 16, 150.25)
    ]
    
    #Create an odd number of Carpet objects
    carpets = [
        Carpet(18, 10, 20.59),
        Carpet(17, 5, 15),
        Carpet(10, 12, 30)
    ]
    
    #Combine the rugs and carpets into a single list
    items = rugs + carpets

    #Puts the items into an empty array to convert to a string
    list = ""
    
    #Iterate through the list and print the description of each item
    for item in items:
        list += str(item) + '\n'

    #prints the list of items
    print(list)

#Runs the main method
if __name__ == "__main__":
    main()