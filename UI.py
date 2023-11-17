from PointRepository import PointRepository
from tests import run_all_tests
from colorama import Fore, Style

def menu():
    print(Fore.YELLOW)
    print("0. Exit")
    print("1. Show all points")
    print("2. Add a point")
    print("3. Show point at a given index")
    print("4. Show all points of a given color")
    print("5. Show all points that are inside a given square")
    print("6. Show the minimum distance between two out of all the points")
    print("7. Update a point at a given index")
    print("8. Delete a point at a given index")
    print("9. Delete all points inside a square")
    print("10. Plot all points in a chart")
    print("11. Show all points inside a given circle")
    print("12. Show all points inside a given rectangle")
    print("13. Show the maximum distance between two out of all the points")
    print("14. Get the number of points of a given color")
    print("15. Update the color of a point given by its coordinates")
    print("16. Shift all points on the X axis")
    print("17. Shift all points on the Y axis")
    print("18. Delete a point by its coordinates")
    print("19. Delete all points inside a circle")
    print("20. Delete all points within a given distance of a point")
    print(Style.RESET_ALL)

def UI():
    #run_all_tests()
    repo = PointRepository()   
    repo.add_point(1, 2, "red")
    repo.add_point(2, 3, "blue")
    repo.add_point(3, 4, "red")
    repo.add_point(4, 5, "blue")
    repo.add_point(5, 6, "red")
    repo.add_point(6, 7, "blue")
    while True:
        try: 
            menu()
            command = int(input("Enter command: "))
            if command == 0:
                break
            elif command == 1:
                print("All points:")
                print(repo.get_all_points())
            elif command == 2:
                coord_X = int(input("Enter coord_X: "))
                coord_Y = int(input("Enter coord_Y: "))
                try:
                    color = input("Enter color: ")
                    if color != "red" and color != "blue" and color != "yellow" and color != "green" and color != "purple" and color != "magenta" and color != "cyan":
                        raise Exception("Invalid color!")
                except Exception as e:
                    print(e)
                    continue
                repo.add_point(coord_X, coord_Y, color)
            elif command == 3:
                index = int(input("Enter index: "))
                print(repo.get_point(index))
            elif command == 4:
                color = str(input("Enter color: "))
                print(repo.get_points_by_color(color))
            elif command == 5:
                coord_X = int(input("Enter coord_X: "))
                coord_Y = int(input("Enter coord_Y: "))
                length = int(input("Enter length: "))
                print(repo.get_points_inside_square(coord_X, coord_Y, length))
            elif command == 6:
                print(repo.get_min_distance())
            elif command == 7:
                index = int(input("Enter index: "))
                coord_X = int(input("Enter coord_X: "))
                coord_Y = int(input("Enter coord_Y: "))
                color = input("Enter color: ")
                repo.update_point(index, coord_X, coord_Y, color)
            elif command == 8:
                index = int(input("Enter index: "))
                repo.delete_point(index)
            elif command == 9:
                coord_X = int(input("Enter coord_X: "))
                coord_Y = int(input("Enter coord_Y: "))
                length = int(input("Enter length: "))
                repo.delete_points_inside_square(coord_X, coord_Y, length)
            elif command == 10:
                repo.plot_points()
            elif command == 11:
                coord_X = int(input("Enter coord_X: "))
                coord_Y = int(input("Enter coord_Y: "))
                radius = int(input("Enter radius: "))
                print(repo.get_points_inside_circle(coord_X, coord_Y, radius))
            elif command == 12:
                coord_X = int(input("Enter coord_X: "))
                coord_Y = int(input("Enter coord_Y: "))
                length = int(input("Enter length: "))
                width = int(input("Enter width: "))
                print(repo.get_points_rectangle(coord_X, coord_Y, length, width))
            elif command == 13:
                print(repo.get_max_distance())
            elif command == 14:
                color = str(input("Enter color: "))
                print(repo.get_points_by_color(color))
            elif command == 15:
                coord_X = int(input("Enter coord_X: "))
                coord_Y = int(input("Enter coord_Y: "))
                color = input("Enter color: ")
                repo.update_color(coord_X, coord_Y, color)
            elif command == 16:
                shift_X = int(input("Enter shift_X: "))
                repo.shift_X(shift_X)
            elif command == 17:
                shift_Y = int(input("Enter shift_Y: "))
                repo.shift_Y(shift_Y)
            elif command == 18:
                coord_X = int(input("Enter coord_X: "))
                coord_Y = int(input("Enter coord_Y: "))
                repo.delete_point_by_coordinates(coord_X, coord_Y)
            elif command == 19:
                coord_X = int(input("Enter coord_X: "))
                coord_Y = int(input("Enter coord_Y: "))
                radius = int(input("Enter radius: "))
                repo.delete_points_inside_circle(coord_X, coord_Y, radius)
            elif command == 20:
                coord_X = int(input("Enter coord_X: "))
                coord_Y = int(input("Enter coord_Y: "))
                length = int(input("Enter length: "))
                repo.delete_points_within_distance(coord_X, coord_Y, length)
            elif command > 20 or command < 0:
                raise ValueError("Invalid command!")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)