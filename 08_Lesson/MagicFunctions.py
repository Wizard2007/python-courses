class ReporMixin:
    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ", ".join(f"{name}={value}" for name , value in vars(self).items())
        )

class Number(ReporMixin):
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        if hasattr(other, 'value'):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        return NotImplemented