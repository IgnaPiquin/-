import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    
    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            picture = ""
            for i in range( self.height):
                picture += "*"  * self.width + f"\n"
        else: 
            return "Too big for picture."
        
        return picture
            
    
    def get_amount_inside(self, shape):
        if self.width < shape.width or self.height < shape.height:
            return 0
        else:
            amount_inside = math.floor(self.width/shape.width) * math.floor(self.height/shape.height)
        
        return amount_inside

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width =side
    
    def set_width(self, width):
        self.width = width
        self.height = width
        
    def set_height(self, height):
        self.height = height
        self.width = height
    
    
    def set_side(self, side):
        self.height = side
        self.width = side
        
    def __str__(self):
        return f"Square(side={self.height})"