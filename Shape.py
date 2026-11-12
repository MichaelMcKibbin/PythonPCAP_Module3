class Shape:
    def __init__(self, name, shape_type, color='Red'):
        self.name = name
        self.shape_type = shape_type
        self.color = color

    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self):
        return f"Shape: {self.name}"

    def get_type(self):
        return self.shape_type

    def get_color(self):
        return self.color

    def get_area(self):
        return self.area()

    def get_perimeter(self):
        return self.perimeter()
