class Reflector:

    def __init__(self, wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring

    def reflect(self, number):
        alphabet = self.right[number]
        number = self.left.find(alphabet)
        return number
