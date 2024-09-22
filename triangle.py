def area(a, h):
    '''
    Returns area of triangle.
        
        Parameters:
            a (int | float): base of triangle
            h (int | float): height of triangle which is drawn to the base

        Result:
            area (float): the area of this triangle
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Returns perimeter of triangle.

        Parameters:
            a, b, c (int | float): sides of a triangle

        Result:
            perimeter (int | float): the perimeter of this triangle
    '''
    return a + b + c
