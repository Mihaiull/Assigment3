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
        lst = []
        for point in self.__points:
            if point.get_coord_X() >= coord_X and point.get_coord_X() <= coord_X + length and point.get_coord_Y() <= coord_Y and point.get_coord_Y() >= coord_Y - length:
                lst.append(point)
        return lst
        
    #Get the minimum distance between two out of all the points:
    #@Output - float
    def get_min_distance(self):
        min_distance = min(get_distance(self.__points[0], self.__points[1]), 9999999)
        for i in range(1, len(self.__points)):
            for j in range(i + 1, len(self.__points)):
                min_distance = min(min_distance, get_distance(self.__points[i], self.__points[j]))
        return min_distance

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
            if point in self.get_points_inside_square(coord_X, coord_Y, length):
                self.__points.remove(point)
    
    #Plot all points in a chart (using matplotlib):
    def plot_points(self):
        x = [point.get_coord_X() for point in self.__points]
        y = [point.get_coord_Y() for point in self.__points]
        col = [point.get_color() for point in self.__points]
        plt.scatter(x, y, c = col)
        plt.show()
        
    #Get all points that are inside a given circle
    #@Input - coord_X: int
    #@Input - coord_Y: int
    #@Input - radius: int
    #@Output - list of MyPointClass
    def get_points_inside_circle(self, coord_X, coord_Y, radius):
        return [point for point in self.__points if get_distance(point, MyPointClass(coord_X, coord_Y, "black")) <= radius]

    #Get all points that are inside a given rectangle
    #@Input - coord_X: int
    #@Input - coord_Y: int
    #(coord_X, coord_Y) is the top-left corner of the rectangle
    #@Input - length: int
    #@Input - width: int
    #@Output - list of MyPointClass
    def get_points_rectangle(self, coord_X, coord_Y, length, width):
        return [point for point in self.__points if point.get_coord_X() >= coord_X and point.get_coord_X() <= coord_X + length and point.get_coord_Y() <= coord_Y and point.get_coord_Y() >= coord_Y - width]
    
    #Get the maximum distance between two out of all the points:
    #@Output - float
    def get_max_distance(self):
        for i in range(len(self.__points)):
            for j in range(i + 1, len(self.__points)):
                if i == 0 and j == 1:
                    max_distance = get_distance(self.__points[i], self.__points[j])
                else:
                    max_distance = max(max_distance, get_distance(self.__points[i], self.__points[j]))
        return max_distance
    
    #Get the number of points of a given color:
    #@Input - color: string
    #@Output - int
    def get_number_of_points_of_color(self, color):
        return len(self.get_points_by_color(color))
    
    #Update the color of a point given by it's coordinates:
    #@Input - coord_X: int
    #@Input - coord_Y: int
    #@Input - color: string
    def update_color(self, coord_X, coord_Y, color):
        for point in self.__points:
            if point.get_coord_X() == coord_X and point.get_coord_Y() == coord_Y:
                point.set_color(color)
    
    #Shift all points on the X axis by a given value:
    #@Input - shift: int
    def shift_X(self, shift):
        for point in self.__points:
            point.set_coord_X(point.get_coord_X() + shift)
    
    #Shift all points on the Y axis by a given value:
    #@Input - shift: int
    def shift_Y(self, shift):
        for point in self.__points:
            point.set_coord_Y(point.get_coord_Y() + shift)
    
    #Delete a point by it's coordintes:
    #@Input - coord_X: int
    #@Input - coord_Y: int
    def delete_point_by_coordinates(self, coord_X, coord_Y):
        for point in self.__points:
            if point.get_coord_X() == coord_X and point.get_coord_Y() == coord_Y:
                self.__points.remove(point)

    #Delete all points that are inside a given circle:
    #@Input - coord_X: int
    #@Input - coord_Y: int
    #@Input - radius: int
    def delete_points_inside_circle(self, coord_X, coord_Y, radius):
        for point in self.__points:
            if point in self.get_points_inside_circle(coord_X, coord_Y, radius):
                self.__points.pop(point)
                
    #Delete all points within a given distance of a given point:
    #@Input - coord_X: int
    #@Input - coord_Y: int
    #@Input - distance: int
    def delete_points_within_distance(self, coord_X, coord_Y, distance):
        for point in self.__points:
            if get_distance(point, MyPointClass(coord_X, coord_Y, "black")) <= distance:
                self.__points.remove(point)
                
    def clear(self):
        self.__points.clear()