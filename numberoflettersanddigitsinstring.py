def count_digits_and_letters(string):
    num_letters = sum(1 for char in string if char.isalpha())
    num_digits = sum(1 for char in string if char.isdigit())
    return num_letters, num_digits

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    letters, digits = count_digits_and_letters(input_string)
    print("Letters:", letters)
    print("Digits:", digits)
