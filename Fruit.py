# This is a class heirarchy example utilizing classes and methods

class Fruit
    def __init__(self, name, color)
        self.name = name
        self.color = color
        self.flavor = 'tasteless'
        self.smell = 'odorless'

    # Setters, these set the values of Fruits' attributes
    def named(self, fruit_name)
        self.name = fruit_name

    def colored(self, fruit_colr)
        self.color = fruit_colr

    def flavored(self, taste)
        self.flavor = taste

    def smelled(self, smell)
        self.smell = smell

    # Defines the description of the fruit
    def describe(self)
        print 'This is a', self.color + self.name, 'it is', self.flavor, 'and smells', self.smell, '.\n'

    
