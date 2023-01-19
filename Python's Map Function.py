def make_even_num(num):
    if num% 2 == 1:
        return num+1
    elif num% 2 == 0:
        return num

x = [21,23,34,34,54,54,6,23,12,34,45,46,56,67]
# creates the map object to conserve memory 
# Convert map object into list and print.
y = list(map(make_even_num, x))
print(y)