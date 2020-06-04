class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"start drawing with a {self.title}"

class Pencil(Stationary):
    def draw(self):
        return f"Started drawing with a {self.title} pencil"

class Pen(Stationary):
    def draw(self):
        return f"Started drawing with a {self.title} pen"

class Marker(Stationary):
    def draw(self):
        return f"Started drawing with a {self.title} marker"

pen = Pen("blue")
pencil = Pencil("simple")
marker = Marker("bright")
print(pen.draw())
print(pencil.draw())
print(marker.draw())
