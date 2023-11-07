from PointRepository import PointRepository

def test_add():
    repo = PointRepository()
    repo.add_point(1, 2, "red")
    assert repo.get_all_points() == [(1, 2, "red")], "Add function does not work correctly! (1)"
    repo.add_point(2, 3, "blue")
    assert repo.get_all_points() == [(1, 2, "red"), (2, 3, "blue")], "Add function does not work correctly! (2)"
    repo.add_point(3, 4, "red")
    assert repo.get_all_points() == [(1, 2, "red"), (2, 3, "blue"), (3, 4, "red")], "Add function does not work correctly! (3)"
    
def test_get_point():
    repo = PointRepository()
    repo.add_point(1, 2, "red")
    repo.add_point(2, 3, "blue")
    repo.add_point(3, 4, "red")
    assert repo.get_point(0) == (1, 2, "red"), "Get point function does not work correctly! (1)"
    assert repo.get_point(1) == (2, 3, "blue"), "Get point function does not work correctly! (2)"
    assert repo.get_point(2) == (3, 4, "red"), "Get point function does not work correctly! (3)"

def test_get_points_by_color():
    repo = PointRepository() 
    repo.add_point(1, 2, "red")
    repo.add_point(2, 3, "blue")
    repo.add_point(3, 4, "red")
    assert repo.get_points_by_color("red") == [(1, 2, "red"), (3, 4, "red")], "Get points by color function does not work correctly! (1)"
    assert repo.get_points_by_color("blue") == [(2, 3, "blue")], "Get points by color function does not work correctly! (2)"
    assert repo.get_points_by_color("green") == [], "Get points by color function does not work correctly! (3)"
    
def test_get_points_inside_square():
    repo = PointRepository()
    repo.add_point(1, 2, "red")
    repo.add_point(2, 3, "blue")
    repo.add_point(3, 4, "red")
    repo.add_point(4, 5, "green")
    repo.add_point(5, 6, "red")
    assert repo.get_points_inside_square(1, 2, 2) == [(1, 2, "red"), (2, 3, "blue")], "Get points inside square function does not work correctly! (1)"
    assert repo.get_points_inside_square(3, 4, 2) == [(3, 4, "red"), (4, 5, "green")], "Get points inside square function does not work correctly! (2)"
    assert repo.get_points_inside_square(5, 6, 2) == [(5, 6, "red")], "Get points inside square function does not work correctly! (3)"
    
def test_get_min_distance():
    repo = PointRepository()
    repo.add_point(1, 2, "red")
    repo.add_point(2, 3, "blue")
    repo.add_point(3, 4, "red")
    repo.add_point(4, 5, "green")
    repo.add_point(5, 6, "red")
    assert repo.get_min_distance() == 1.4142135623730951, "Get min distance function does not work correctly! (1)"
    repo.clear()
    repo.add_point(1, 2, "red")
    repo.add_point(3, 3, "blue")
    assert repo.get_min_distance() == 2.23606797749979, "Get min distance function does not work correctly! (2)"
    repo.clear()
    repo.add_point(12, 2, "red")
    repo.add_point(3, 3, "blue")
    repo.add_point(3, 4, "red")
    
def test_update_point():
    repo = PointRepository()
    repo.add_point(1, 2, "red")
    repo.add_point(2, 3, "blue")
    repo.add_point(3, 4, "red")
    repo.update_point(1, 4, 5, "green")
    assert repo.get_all_points() == [(1, 2, "red"), (4, 5, "green"), (3, 4, "red")], "Update point function does not work correctly! (1)"
    
def test_delete_point():
    repo = PointRepository()
    repo.add_point(1, 2, "red")
    repo.add_point(2, 3, "blue")
    repo.add_point(3, 4, "red")
    repo.delete_point(1)
    assert repo.get_all_points() == [(1, 2, "red"), (3, 4, "red")], "Delete point function does not work correctly! (1)"
    
def test_delete_points_inside_square():
    repo = PointRepository()
    repo.add_point(1, 2, "red")
    repo.add_point(2, 3, "blue")
    repo.add_point(3, 4, "red")
    repo.add_point(4, 5, "green")
    repo.add_point(5, 6, "red")
    repo.delete_points_inside_square(1, 2, 2)
    assert repo.get_all_points() == [(3, 4, "red"), (4, 5, "green"), (5, 6, "red")], "Delete points inside square function does not work correctly! (1)"