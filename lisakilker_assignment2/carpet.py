#Carpet class file
#Imports Rectangle class file
from rectangle import Rectangle

class Carpet(Rectangle):
    
    #Initializer
    def __init__(self, carpet_length, carpet_width, carpet_price_per_sq_ft):
        Rectangle.__init__(self, carpet_length, carpet_width)
        self.__carpet_price_per_sq_ft = carpet_price_per_sq_ft
        self.__carpet_price_per_sq_ft = carpet_price_per_sq_ft
    
    #Gets the carpet price
    def get_carpet_price_per_square_foot(self):
        return self.__carpet_price_per_sq_ft
    
    #Gets the total price based on the sq footage area of the rug
    def get_total_price(self):
        return self.get_area() * self.__carpet_price_per_sq_ft
    
    #Overrider that returns a string method with the description of the carpet
    def __str__(self):
        return f"Carpet - Dimensions: {self.get_length()}x{self.get_width()}, Price per sqft: ${self.__carpet_price_per_sq_ft:.2f}, Total Price: ${self.get_total_price():.2f}"