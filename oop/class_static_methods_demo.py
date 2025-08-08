class Calculator:
    """
    Calculator class demonstrating static and class methods.
    """
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Does not require access to class or instance attributes.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Has access to class attributes and can be used for factory methods.
        
        Args:
            cls: The class itself
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
