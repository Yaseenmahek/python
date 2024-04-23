def sum_numbers(lst):
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

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
sum_numbers(numbers)
