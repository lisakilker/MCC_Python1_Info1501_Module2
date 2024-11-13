#Rectangle class file
class Rectangle:
    
    #Initializer
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    #Gets length
    def get_length(self):
        return self.__length

    #Sets length
    def set_length(self, length):
        self.__length = length

    #Gets width
    def get_width(self):
        return self.__width

    #Sets width
    def set_width(self, width):
        self.__width = width

    #Gets area (area set in another class)
    def get_area(self):
        return self.__length * self.__width
    