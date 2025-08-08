import math

class Shape:
    """
    Base class for geometric shapes.
    """
    
    def area(self):
        """
        Calculate the area of the shape.
        This method should be overridden by derived classes.
        
        Raises:
            NotImplementedError: Indicates that derived classes must override this method
        """
        raise NotImplementedError("Subclasses must override area() method")


class Rectangle(Shape):
    """
    Derived class representing a rectangle.
    Inherits from Shape and overrides the area() method.
    """
    
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """
    Derived class representing a circle.
    Inherits from Shape and overrides the area() method.
    """
    
    def __init__(self, radius):
        """
        Initialize a Circle instance.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²)
        """
        return math.pi * self.radius ** 2
