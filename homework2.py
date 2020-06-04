class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        print (f"Mass of asphalt rquired is {self._length * self._width * 5 * 25 / 1000} tonn")

road = Road(5000, 20)
road.mass()
