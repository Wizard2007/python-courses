class Shape:
    def __init__(self, x, y, **kwargs):        
        self.x, self.y = x,y
        super().__init__(**kwargs)


class Circle(Shape):
    def __init__(self, r, **kwargs):        
        self.r = r
        super().__init__(**kwargs)


class ColoredShape(Shape):
    def __init__(self,color, **kwargs):        
        self.color = color
        super().__init__(**kwargs)


class ColoredCircle1(Circle, ColoredShape):
    def __init__(self, x, y, r, color):
        super().__init__(x=x, y=y,r=r,color=color)
