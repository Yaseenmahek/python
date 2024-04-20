a, b, c, d, e = 10, 20, 5, 30, 15
max_num = a if (a > b and a > c and a > d and a > e) else \
          b if (b > c and b > d and b > e) else \
          c if (c > d and c > e) else \
          d if (d > e) else e

print("The greatest number is:", max_num)