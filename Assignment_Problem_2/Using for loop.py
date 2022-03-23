#WAP  to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values
dict_ascii = {}
for i in range(ord('a'),ord('z')+1):
    dict_ascii[chr(i)] = i
print(dict_ascii)