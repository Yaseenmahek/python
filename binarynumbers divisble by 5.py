def binary_divisible_by_5(sequence):
    numbers = sequence.split(",")
    divisible_by_5 = [num for num in numbers if int(num, 2) % 5 == 0]
    return ",".join(divisible_by_5)

if __name__ == "__main__":
    binary_input = input("enter the binary numbers seperated by comma +: ")
    result = binary_divisible_by_5(binary_input)
    print("Numbers divisible by 5:", result)
