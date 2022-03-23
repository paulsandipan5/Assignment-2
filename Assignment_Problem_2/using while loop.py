#WAP  to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values
i = ord('a')
while i < ord('z')+1:
    dict_ascii[chr(i)] = i
    i+=1
print(dict_ascii)
