my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
x = sorted(my_dict, key=(lambda key:my_dict[key]), reverse=True)
print(x[0])
print(x[1])
print(x[2])
