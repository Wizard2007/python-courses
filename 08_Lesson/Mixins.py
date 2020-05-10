class ReporMixin:
    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ", ".join(f"{name}={value}" for name , value in vars(self).items())
        )

class Person(ReporMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age
#    def __repr__(self):
#        return f"Person('{self.name}', '{self.age}')"
    def __str__(self):
        return f"<{self.name}, {self.age}>"