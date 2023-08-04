alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class EnigmaM3:

    def __init__(self, reflector, rotor1, rotor2, rotor3, plugboard, keyboard):
        self.rfl = reflector
        self.rt1 = rotor1
        self.rt2 = rotor2
        self.rt3 = rotor3
        self.plb = plugboard
        self.kyb = keyboard

    def set_keys(self, keys):
        self.rt1.rotate_to_alphabet(keys[0])
        self.rt2.rotate_to_alphabet(keys[1])
        self.rt3.rotate_to_alphabet(keys[2])

    def set_rings(self, rings):
        self.rt1.set_ring(rings[0])
        self.rt2.set_ring(rings[1])
        self.rt3.set_ring(rings[2])
    
    def encrypt(self, alphabet):
        # Rotating
        if (self.rt2.left[0] == self.rt2.turnover_notch and self.rt3.left[0] == self.rt3.turnover_notch):
            self.rt1.rotate()
            self.rt2.rotate()
            self.rt3.rotate()
        elif (self.rt2.left[0] == self.rt2.turnover_notch): # Double Step Anomaly
            self.rt1.rotate()
            self.rt2.rotate()
            self.rt3.rotate()
        elif (self.rt3.left[0] == self.rt3.turnover_notch):
            self.rt2.rotate()
            self.rt3.rotate()
        else:
            self.rt3.rotate()

        # Passing
        steps = ""
        number = self.kyb.forward(alphabet)
        steps += "Alphabet: " + alphabet + "\n"
        number = self.plb.forward(number)
        steps += "Plugboard Encryption: " + alphabets[number] + "\n"
        number = self.rt3.forward(number)
        steps += "Rotor 3 Encryption: " + alphabets[number] + "\n"
        number = self.rt2.forward(number)
        steps += "Rotor 2 Encryption: " + alphabets[number] + "\n"
        number = self.rt1.forward(number)
        steps += "Rotor 1 Encryption: " + alphabets[number] + "\n"
        number = self.rfl.reflect(number)
        steps += "Reflector Encryption: " + alphabets[number] + "\n"
        number = self.rt1.backward(number)
        steps += "Rotor 1 Encryption: " + alphabets[number] + "\n"
        number = self.rt2.backward(number)
        steps += "Rotor 2 Encryption: " + alphabets[number] + "\n"
        number = self.rt3.backward(number)
        steps += "Rotor 3 Encryption: " + alphabets[number] + "\n"
        number = self.plb.backward(number)
        steps += "Plugboard Encryption: " + alphabets[number] + "\n"
        alphabet = self.kyb.backward(number)
        steps += "Output: " + alphabets[number] + "\n"
        
        position = "Rotors Position: " + self.rt1.left[0] + self.rt2.left[0] + self.rt3.left[0] + "\n\n"

        return alphabet, steps, position