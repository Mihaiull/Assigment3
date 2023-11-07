from PointRepository import PointRepository

def menu():
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
    
def UI():
    repo = PointRepository()   
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
                color = input("Enter color: ")
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
            elif command > 10 or command < 0:
                raise ValueError("Invalid command!")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)