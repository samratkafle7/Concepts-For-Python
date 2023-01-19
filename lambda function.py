
add = lambda n1, n2, n3: n1 + n2 +n3

print(add(10, 450, 23))

#Example 2 

numbers = [1, 2, 3, 4, 5, 6]
squared = []
for i in numbers:
    i = i**2
    squared.append(i)
print(squared)

#same example 2 can be written as

squared_num = []

square = lambda n: n**2
for n in numbers:
    squared_num.append(square(n))
print(squared_num)