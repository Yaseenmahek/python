class Mango:
    def _init_(self):
        print("This is what?")

    def balaji(self):
        print("This is without para")

    def shetty(self, a, b):
        print(a + b, "This is with para")

    def magicalprime(self, a):
        print('Check if it is a magical prime or not')

    def neon(self, a):
        square = a ** 2
        sum_of_digits = sum(int(digit) for digit in str(square))
        if sum_of_digits == a:
            print(f"{a} is a neon number.")
        else:
            print(f"{a} is not a neon number.")

man = Mango()
man.balaji()
man.shetty(10, 20.5)
man.magicalprime(101)
man.neon(7)
man.neon(9)