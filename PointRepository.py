from MyPoint import MyPointClass
import matplotlib.pyplot as plt

#Function that computes the distance between two points:
#Will be used in get_min_distance() method
#@Input - point1: MyPointClass
#@Input - point2: MyPointClass
#@Output - float
def get_distance(point1, point2):
    return ((point1.get_coord_X() - point2.get_coord_X()) ** 2 + (point1.get_coord_Y() - point2.get_coord_Y()) ** 2) ** 0.5

class PointRepository():
    def __init__(self):
        self.__points = []
        
    #Add a point to the repository:
    #@Input - point: MyPointClass
    def add_point(self, point):
        self.__points.append(point)
    #Add a point to the repository:(overloaded)
    #@Input - coord_X: int
    #@Input - coord_Y: int
    #@Input - color: string
    def add_point(self, coord_X, coord_Y, color):
        self.__points.append(MyPointClass(coord_X, coord_Y, color))
        
    #Get all points from the repository:
    #@Output - list of MyPointClass
    def get_all_points(self):
        return self.__points

    #Get a point at a given index:
    #@Input - index: int
    #@Output - MyPointClass
    def get_point(self, index):
        return self.__points[index]
    
    #Get all points of a given color:
    #@Input - color: string
    #@Output - list of MyPointClass
    def get_points_by_color(self, color):
        return [point for point in self.__points if point.get_color() == color]
    
    #Get all points that are inside a given square:
    #@Input - coord_X: int
    #@Input - coord_Y: int
    #(coord_X, coord_Y) is the top-left corner of the square
    #@Input - length: int
    #@Output - list of MyPointClass
    def get_points_inside_square(self, coord_X, coord_Y, length):
        return [point for point in self.__points if point.get_coord_X() >= coord_X and point.get_coord_X() <= coord_X + length and point.get_coord_Y() <= coord_Y and point.get_coord_Y() >= coord_Y - length]
        
    #Get the minimum distance between two out of all the points:
    #@Output - float
    def get_min_distance(self):
        for i in range(len(self.__points)):
            for j in range(i + 1, len(self.__points)):
                if i == 0 and j == 1:
                    min_distance = get_distance(self.__points[i], self.__points[j])
                else:
                    min_distance = min(min_distance, get_distance(self.__points[i], self.__points[j]))
        
    #Update a point at a given index:
    #@Input - index: int
    #@Input - coord_X: int
    #@Input - coord_Y: int
    #@Input - color: string
    def update_point(self, index, coord_X, coord_Y, color):
        self.__points[index].set_coord_X(coord_X)
        self.__points[index].set_coord_Y(coord_Y)
        self.__points[index].set_color(color)
        
    #Delete a point at a given index:
    #@Input - index: int
    def delete_point(self, index):
        del self.__points[index]
    
    #Delete all points that are inside a given square:
    #@Input - coord_X: int
    #@Input - coord_Y: int
    #(coord_X, coord_Y) is the top-left corner of the square
    #@Input - length: int
    def delete_points_inside_square(self, coord_X, coord_Y, length):
        for point in self.__points:
            if point.get_coord_X() >= coord_X and point.get_coord_X() <= coord_X + length and point.get_coord_Y() <= coord_Y and point.get_coord_Y() >= coord_Y + length:
                self.__points.remove(point)
    
    #Plot all points in a chart (using matplotlib):
    def plot_points(self):
        x = [point.get_coord_X() for point in self.__points]
        y = [point.get_coord_Y() for point in self.__points]
        col = [point.get_color() for point in self.__points]
        plt.scatter(x, y, c = col)
        plt.show()