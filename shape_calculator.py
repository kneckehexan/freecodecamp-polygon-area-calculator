class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        
        lines = ''
        for h in range(self.height):
            lines += '*' * self.width + '\n'

        return lines
    
    def get_amount_inside(self, shape):
        w = self.width//shape.width
        h = self.height//shape.height

        return w*h
    
    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

class Square(Rectangle):

    def __init__(self, length):
        self.width = length
        self.height = length
    
    def set_side(self, side):
        self.height = side
        self.width = side

    def __str__(self):
        return 'Square(side=' + str(self.width) + ')'
