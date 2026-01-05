class Pozycja:
        def __init__(self,x,y):
            self.x = x
            self.y = y
        def __eq__(self, reszta):
            return isinstance(reszta, Pozycja) and self.x==reszta.x and self.y==reszta.y
        def __str__(self):
            return f"({self.x},{self.y})"
        __repr__ = __str__
