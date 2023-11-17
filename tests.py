from PointRepository import PointRepository
from MyPoint import MyPointClass
from colorama import Fore, Style

def test_add():
    repo = PointRepository()
    repo.add_point (1, 2, 'red')
    actual = repo.get_all_points()
    expected = [MyPointClass(1, 2, 'red')]
    assert actual[0] == expected[0], 'Add function does not work correctly! (1)'
    repo.add_point(2, 3, 'blue')
    actual = repo.get_all_points()
    expected = [MyPointClass(1, 2, 'red'), MyPointClass(2, 3, 'blue')]
    assert actual == expected, 'Add function does not work correctly! (2)'
    repo.add_point(3, 4, 'red')
    actual = repo.get_all_points()
    expected = [MyPointClass(1, 2, 'red'), MyPointClass(2, 3, 'blue'), MyPointClass(3, 4, 'red')]
    assert actual == expected, 'Add function does not work correctly! (3)'
def test_get_point():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'blue')
    repo.add_point(3, 4, 'red')
    assert repo.get_point(0) == MyPointClass(1, 2, 'red'), 'Get point function does not work correctly! (1)'
    assert repo.get_point(1) == MyPointClass(2, 3, 'blue'), 'Get point function does not work correctly! (2)'
    assert repo.get_point(2) == MyPointClass(3, 4, 'red'), 'Get point function does not work correctly! (3)'

def test_get_points_by_color():
    repo = PointRepository() 
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'blue')
    repo.add_point(3, 4, 'red')
    assert repo.get_points_by_color('red') == [MyPointClass(1, 2, 'red'), MyPointClass(3, 4, 'red')], 'Get points by color function does not work correctly! (1)'
    assert repo.get_points_by_color('blue') == [MyPointClass(2, 3, 'blue')], 'Get points by color function does not work correctly! (2)'
    assert repo.get_points_by_color('green') == [], 'Get points by color function does not work correctly! (3)'
    
def test_get_points_inside_square():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'blue')
    repo.add_point(3, 4, 'red')
    repo.add_point(4, 5, 'green')
    repo.add_point(5, 6, 'red')
    assert repo.get_points_inside_square(1, 2, 2) == [MyPointClass(1, 2, 'red')], 'Get points inside square function does not work correctly! (1)'
    assert repo.get_points_inside_square(3, 4, 2) == [MyPointClass(3, 4, 'red')], 'Get points inside square function does not work correctly! (2)'
    assert repo.get_points_inside_square(1, 6, 10) == [MyPointClass(1, 2,'red'), MyPointClass(2, 3, 'blue'), MyPointClass(3, 4, 'red'), MyPointClass(4, 5, 'green'), MyPointClass(5, 6, 'red')], 'Get points inside square function does not work correctly! (3)'
    
def test_get_min_distance():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'blue')
    repo.add_point(3, 4, 'red')
    repo.add_point(4, 5, 'green')
    repo.add_point(5, 6, 'red')
    assert repo.get_min_distance() == 1.4142135623730951, 'Get min distance function does not work correctly! (1)'
    repo.clear()
    repo.add_point(1, 2, 'red')
    repo.add_point(3, 3, 'blue')
    assert repo.get_min_distance() == 2.23606797749979, 'Get min distance function does not work correctly! (2)'
    repo.clear()
    repo.add_point(12, 2, 'red')
    repo.add_point(3, 3, 'blue')
    repo.add_point(3, 4, 'red')
    
def test_update_point():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'blue')
    repo.add_point(3, 4, 'red')
    repo.update_point(1, 4, 5, 'green')
    assert repo.get_all_points() == [MyPointClass(1, 2, 'red'), MyPointClass(4, 5, 'green'), MyPointClass(3, 4, 'red')], 'Update point function does not work correctly! (1)'
    
def test_delete_point():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'blue')
    repo.add_point(3, 4, 'red')
    repo.delete_point(1)
    assert repo.get_all_points() == [MyPointClass(1, 2, 'red'), MyPointClass(3, 4, 'red')], 'Delete point function does not work correctly! (1)'
    
def test_delete_points_inside_square():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'blue')
    repo.add_point(3, 4, 'red')
    repo.add_point(4, 5, 'green')
    repo.add_point(5, 6, 'red')
    repo.delete_points_inside_square(0, 3, 3)

    assert repo.get_all_points() == [MyPointClass(2, 3, 'blue'), MyPointClass(3, 4, 'red'), MyPointClass(4, 5, 'green'), MyPointClass(5, 6, 'red')], 'Delete points inside square function does not work correctly! (1)'
    repo.delete_points_inside_square(3, 6, 3)
    assert repo.get_all_points() == [MyPointClass(2, 3, 'blue'), MyPointClass(4, 5, 'green')], 'Delete points inside square function does not work correctly! (2)'
    repo.clear()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'blue')
    repo.add_point(3, 4, 'red')
    repo.delete_points_inside_square(5, 6, 2)
    assert repo.get_all_points() == [MyPointClass(1, 2, 'red'), MyPointClass(2, 3, 'blue'), MyPointClass(3, 4, 'red')], 'Delete points inside square function does not work correctly! (3)'

def test_get_points_inside_circle():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'blue')
    repo.add_point(3, 4, 'red')
    repo.add_point(4, 5, 'green')
    assert repo.get_points_inside_circle(1, 2, 2) == [MyPointClass(1, 2, 'red'), MyPointClass(2, 3, 'blue')], 'Get points inside circle function does not work correctly! (1)'
    assert repo.get_points_inside_circle(3, 4, 2) == [MyPointClass(2, 3, 'blue') ,MyPointClass(3, 4, 'red'), MyPointClass(4, 5, 'green')], 'Get points inside circle function does not work correctly! (2)'
    assert repo.get_points_inside_circle(5, 6, 1) == [], 'Get points inside circle function does not work correctly! (3)'

def test_get_points_rectangle():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'blue')
    repo.add_point(3, 4, 'red')
    repo.add_point(4, 5, 'green')
    assert repo.get_points_rectangle(1, 2, 2, 2) == [MyPointClass(1, 2, 'red')], 'Get points rectangle function does not work correctly! (1)'
    assert repo.get_points_rectangle(3, 4, 2, 2) == [MyPointClass(3, 4, 'red')], 'Get points rectangle function does not work correctly! (2)'
    assert repo.get_points_rectangle(5, 6, 2, 2) == [], 'Get points rectangle function does not work correctly! (3)'

def test_get_max_distance():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'blue')
    assert repo.get_max_distance() == 1.4142135623730951, 'Get max distance function does not work correctly! (1)'
    repo.add_point(3, 4, 'red')
    assert repo.get_max_distance() == 2.8284271247461903, 'Get max distance function does not work correctly! (2)'
    repo.add_point(4, 5, 'green')
    assert repo.get_max_distance() == 4.242640687119285, 'Get max distance function does not work correctly! (3)'

def test_get_number_of_points_of_color():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'red')
    repo.add_point(3, 4, 'blue')
    repo.add_point(4, 5, 'green')
    repo.add_point(5, 6, 'red')
    assert repo.get_number_of_points_of_color('red') == 3, 'Get number of points of color function does not work correctly! (1)'
    assert repo.get_number_of_points_of_color('blue') == 1, 'Get number of points of color function does not work correctly! (2)'
    assert repo.get_number_of_points_of_color('green') == 1, 'Get number of points of color function does not work correctly! (3)'

def test_update_color():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'red')
    repo.add_point(3, 4, 'blue')
    repo.add_point(4, 5, 'green')
    repo.add_point(5, 6, 'red')
    repo.update_color(1, 2, 'green')
    assert repo.get_all_points() == [MyPointClass(1, 2, 'green'), MyPointClass(2, 3, 'red'), MyPointClass(3, 4, 'blue'), MyPointClass(4, 5, 'green'), MyPointClass(5, 6, 'red')], 'Update color function does not work correctly! (1)'
    repo.update_color(2, 3, 'blue')
    assert repo.get_all_points() == [MyPointClass(1, 2, 'green'), MyPointClass(2, 3, 'blue'), MyPointClass(3, 4, 'blue'), MyPointClass(4, 5, 'green'), MyPointClass(5, 6, 'red')], 'Update color function does not work correctly! (2)'
    repo.update_color(3, 4, 'red')
    assert repo.get_all_points() == [MyPointClass(1, 2, 'green'), MyPointClass(2, 3, 'blue'), MyPointClass(3, 4, 'red'), MyPointClass(4, 5, 'green'), MyPointClass(5, 6, 'red')], 'Update color function does not work correctly! (3)'

def test_shift_X():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'red')
    repo.add_point(3, 4, 'blue')
    repo.add_point(4, 5, 'green')
    repo.shift_X(1)
    assert repo.get_all_points() == [MyPointClass(2, 2, 'red'), MyPointClass(3, 3, 'red'), MyPointClass(4, 4, 'blue'), MyPointClass(5, 5, 'green')], 'Shift X function does not work correctly! (1)'
    repo.shift_X(2)
    assert repo.get_all_points() == [MyPointClass(4, 2, 'red'), MyPointClass(5, 3, 'red'), MyPointClass(6, 4, 'blue'), MyPointClass(7, 5, 'green')], 'Shift X function does not work correctly! (2)'
    repo.shift_X(3)
    assert repo.get_all_points() == [MyPointClass(7, 2, 'red'), MyPointClass(8, 3, 'red'), MyPointClass(9, 4, 'blue'), MyPointClass(10, 5, 'green')], 'Shift X function does not work correctly! (3)'

def test_shift_Y():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'red')
    repo.add_point(3, 4, 'blue')
    repo.shift_Y(1)
    assert repo.get_all_points() == [MyPointClass(1, 3, 'red'), MyPointClass(2, 4, 'red'), MyPointClass(3, 5, 'blue')], 'Shift Y function does not work correctly! (1)'
    repo.shift_Y(2)
    assert repo.get_all_points() == [MyPointClass(1, 5, 'red'), MyPointClass(2, 6, 'red'), MyPointClass(3, 7, 'blue')], 'Shift Y function does not work correctly! (2)'
    repo.shift_Y(3)
    assert repo.get_all_points() == [MyPointClass(1, 8, 'red'), MyPointClass(2, 9, 'red'), MyPointClass(3, 10, 'blue')], 'Shift Y function does not work correctly! (3)'

def test_delete_point_by_coordinates():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.delete_point_by_coordinates(1, 2)
    assert repo.get_all_points() == [], 'Delete point by coordinates function does not work correctly! (1)'
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'red')
    repo.delete_point_by_coordinates(1, 2)
    assert repo.get_all_points() == [MyPointClass(2, 3, 'red')], 'Delete point by coordinates function does not work correctly! (2)'
    repo.add_point(1, 2, 'red')
    repo.delete_point_by_coordinates(2, 3)
    assert repo.get_all_points() == [MyPointClass(1, 2, 'red')], 'Delete point by coordinates function does not work correctly! (3)'

def test_delete_points_inside_circle():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.delete_points_inside_circle(1, 2, 2)
    assert repo.get_all_points() == [], 'Delete points inside circle function does not work correctly! (1)'
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'red')
    repo.delete_points_inside_circle(1, 2, 2)
    assert repo.get_all_points() == [MyPointClass(2, 3, 'red')], 'Delete points inside circle function does not work correctly! (2)'
    repo.add_point(1, 2, 'red')
    repo.delete_points_inside_circle(2, 3, 2)
    assert repo.get_all_points() == [MyPointClass(1, 2, 'red')], 'Delete points inside circle function does not work correctly! (3)'

def test_delete_points_within_distance():
    repo = PointRepository()
    repo.add_point(1, 2, 'red')
    repo.delete_points_within_distance(1, 2, 2)
    assert repo.get_all_points() == [], 'Delete points within distance function does not work correctly! (1)'
    repo.add_point(1, 2, 'red')
    repo.add_point(2, 3, 'red')
    repo.delete_points_within_distance(1, 2, 2)
    assert repo.get_all_points() == [MyPointClass(2, 3, 'red')], 'Delete points within distance function does not work correctly! (2)'
    repo.add_point(1, 2, 'red')
    repo.delete_points_within_distance(2, 3, 2)
    assert repo.get_all_points() == [MyPointClass(1, 2, 'red')], 'Delete points within distance function does not work correctly! (3)'
def run_all_tests():
    try:
        test_add()
        test_get_point()
        test_get_points_by_color()
        test_get_points_inside_square()
        test_get_min_distance()
        test_update_point()
        test_delete_point()
        test_delete_points_inside_square()
        test_get_points_inside_circle()
        test_get_points_rectangle()
        test_get_max_distance()
        test_get_number_of_points_of_color()
        test_update_color()
        test_shift_X()
        test_shift_Y()
        test_delete_point_by_coordinates()
        test_delete_points_inside_circle()
        test_delete_points_within_distance()
    except AssertionError as e:
        print(Fore.RED + str(e) + Style.RESET_ALL)