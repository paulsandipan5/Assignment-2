#WAP using while loop
i = ord('a')
while i < ord('z')+1:
    dict_ascii[chr(i)] = i
    i+=1
print(dict_ascii)