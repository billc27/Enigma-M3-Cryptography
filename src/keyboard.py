class Keyboard:
    
    def forward(self, alphabet):
        number = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(alphabet)
        return number
    
    def backward(self, number):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[number]
        return alphabet