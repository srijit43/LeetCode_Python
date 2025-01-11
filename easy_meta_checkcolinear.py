# Given an array containing exactly three unique points, each represented as 
# coordinate pairs (x, y) with no duplicates, determine whether these points lie on the same straight line. Return True if they do, and False otherwise.

def on_straight_line(points):
    """
    Determines whether three points lie on the same straight line.

    :param points: List of tuples [(x1, y1), (x2, y2), (x3, y3)]
    :return: True if the points are collinear, False otherwise
    """
    if len(points) != 3:
        raise ValueError("The input must contain exactly three points.")
    
    (x1, y1), (x2, y2), (x3, y3) = points

    # Check for collinearity using the determinant method
    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)