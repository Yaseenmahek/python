def sum_numbers():
    lst = input("Enter numbers separated by spaces: ").split()
    lst = [int(x) for x in lst]  # Convert input strings to integers
    sum_negative = 0
    sum_positive_even = 0
    sum_positive_odd = 0
    
    for num in lst:
        if num < 0:
            sum_negative += num
        elif num % 2 == 0:
            sum_positive_even += num
        else:
            sum_positive_odd += num
    
    print("Sum of negative numbers:", sum_negative)
    print("Sum of positive even numbers:", sum_positive_even)
    print("Sum of positive odd numbers:", sum_positive_odd)


sum_numbers()