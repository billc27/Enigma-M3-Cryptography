class Rotor:

    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.turnover_notch = notch

    def forward(self, number):
        alphabet = self.right[number]
        number = self.left.find(alphabet)
        return number
    
    def backward(self, number):
        alphabet = self.left[number]
        number = self.right.find(alphabet)
        return number
    
    def rotate(self, n = 1, forward = True):
        for i in range(n):
            if (forward):
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]

    def display(self):
        print(self.left)
        print(self.right)
        print("")

    def set_ring(self, position_n):
        # Rotating the rotor backwards
        self.rotate(position_n-1, False)

        # Adjusting the notch in relationship to the wiring
        n_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.turnover_notch)
        self.turnover_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(n_notch - position_n + 1) % 26]

    def rotate_to_alphabet(self, alphabet):
        rotations_num = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(alphabet)
        self.rotate(rotations_num)

