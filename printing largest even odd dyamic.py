def largest_even_and_odd(lst):
    largest_even = float('-inf')
    largest_odd = float('-inf')
    
    for num in lst:
        if num % 2 == 0 and num > largest_even:
            largest_even = num
        elif num % 2 != 0 and num > largest_odd:
            largest_odd = num
    
    if largest_even != float('-inf'):
        print("Largest even number:", largest_even)
    else:
        print("No even numbers in the list")
    
    if largest_odd != float('-inf'):
        print("Largest odd number:", largest_odd)
    else:
        print("No odd numbers in the list")


lst = input("Enter numbers separated by spaces: ").split()
try:
    lst = [int(x) for x in lst]
    largest_even_and_odd(lst)
except ValueError:
    print("Please enter valid integers separated by spaces.")
