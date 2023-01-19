N = input("Enter num.").split()
converted_list_int = list(map(int, N))
print(converted_list_int)
converted_tuple = tuple(converted_list_int)
print(converted_tuple)

print(hash(converted_tuple))