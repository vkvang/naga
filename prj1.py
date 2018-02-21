from __future__ import print_function
from __future__ import division

'''
    Setting up a class:
    
        To create a class, we use the 'class :' to set up object
            Then can use the '__init__' method to create and 
            start variables unique to class
            
        Then use 'def():' to name the methods of the class
            indentation is important to maintaining class 
            functionality
'''



# Example Class

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = 'This shape has not been described yet.'
        self.author = 'Nobody has claimed to make this shape yet.'

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale

# Example of implimentation

length = 10
width = 10

# Called upon the new class, initializing it
rectangle = Shape(length, width)
print 'The length is', length, 'and width', width, '.\n'

# Begin to call upon the methods
print 'This is the area: ' , rectangle.area()
print 'This is the perimeter: ' , rectangle.perimeter()

print
rectangle.describe('A rectangular figure.')
print 'This is the description: ' + rectangle.description
rectangle.authorName('Great Gatsby')
print 'This is the author name: ' , rectangle.author

rectangle.scaleSize(2)
print 'The scale is 2: ' + str(rectangle.x) ,'by', str(rectangle.y)

