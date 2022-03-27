# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples(user input available)

l = []
n = int(input("Enter the length of list:"))
for m in range(n):
    print("Enter the element 1 of tuple",m+1,":")
    t_1 = int(input())
    print("Enter the element 2 of tuple",m+1,":")
    t_2 = int(input())
    l.append(tuple([t_1,t_2]))
for i in range(len(l)):
    for j in range(len(l)):
        if l[i][1] < l[j][1]:
            l[i],l[j] = l[j],l[i]
print(l)


# or can be done like
l = []
n = int(input("Enter the length of list:"))
for m in range(n):
    print("Enter the element 1 of tuple",m+1,":")
    t_1 = int(input())
    print("Enter the element 2 of tuple",m+1,":")
    t_2 = int(input())
    l.append((t_1,t_2)) # no need to write tuple here as writen above just follow the syntan properly
for i in range(len(l)):
    for j in range(len(l)):
        if l[i][1] < l[j][1]:
            l[i],l[j] = l[j],l[i]
print(l)
