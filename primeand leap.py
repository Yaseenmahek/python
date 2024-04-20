def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
  if num%4==0 and num%400==0:
      return true

numbers = [2004,1996,17,10,85]

print("Prime numbers in the list:")
for num in numbers:
    if is_prime(num):
        print(num)
    