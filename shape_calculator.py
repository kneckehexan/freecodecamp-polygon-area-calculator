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
        lines = ''
        for h in range(self.height):
            if h == self.height-1:
                lines += '*' * self.width
            else:
                lines += '*' * self.width + '\n'

        return lines
    
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
