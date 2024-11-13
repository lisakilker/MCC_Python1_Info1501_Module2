#Rug class file
#Imports Rectangle class file
from rectangle import Rectangle

class Rug(Rectangle):
    
    #Initializer
    def __init__(self, rug_length, rug_width, rug_price):
        Rectangle.__init__(self, rug_length, rug_width)
        self.__rug_price = rug_price
    
    #Gets the rug price
    def get_rug_price(self):
        return self.__rug_price
    
    #Overrider that returns a string method with the description of the rug
    def __str__(self):
        return (f"Rug - Dimensions: {self.get_length()}x{self.get_width()}, Price: ${self.__rug_price:.2f}")