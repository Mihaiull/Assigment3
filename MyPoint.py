from colorama import Fore, Style


#Class MyPoint that represents a point in a 2D space
#Has the following attributes:
#   - coord_X: int
#   - coord_Y: int
#   - color: string
class MyPointClass():
    def __init__(self, coord_X, coord_Y, color):
        self.__coord_X = coord_X
        self.__coord_Y = coord_Y
        self.__color = color
    
    def get_coord_X(self):
        return self.__coord_X
    def get_coord_Y(self):
        return self.__coord_Y
    def get_color(self):
        return self.__color
    def set_coord_X(self, coord_X):
        self.__coord_X = coord_X
    def set_coord_Y(self, coord_Y):
        self.__coord_Y = coord_Y
    def set_color(self, color):
        self.__color = color
    
    def __str__(self):
        return "(" + str(self.__coord_X) + ", " + str(self.__coord_Y) + ", '" + self.__color + "')"
    def __repr__(self):
        return str(self)
    def __eq__ (self, other):
        return self.__coord_X == other.get_coord_X() and self.__coord_Y == other.get_coord_Y() and self.__color == other.get_color()