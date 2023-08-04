class Plugboard:

    def __init__(self, pairs):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            X = pair[0]
            Y = pair[1]
            position_X = self.left.find(X)
            position_Y = self.right.find(Y)

            # Swapping
            self.left = self.left[:position_X] + Y + self.left[position_X+1:]
            self.left = self.left[:position_Y] + X + self.left[position_Y+1:]

    def forward(self, number):
        alphabet = self.right[number]
        number = self.left.find(alphabet)
        return number
    
    def backward(self, number):
        alphabet = self.left[number]
        number = self.right.find(alphabet)
        return number
    

# Test
# a = Plugboard(["AC"])
# print(a.left, a.right)
# print(a.forward(0))
