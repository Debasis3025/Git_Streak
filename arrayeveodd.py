arr = [1, 2, 3, 4, 5, 6]
c=0
b=0
for i in range(0, len(arr)+1, 2):
    c+=i
    #print(arr[i])
for j in range(1, len(arr)+1, 2):
     b+=j
print(b)
print(c)