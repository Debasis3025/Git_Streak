
arr= []
for num in range(1, 11):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            arr.append(num)


for i in range(0, len(arr), 2):
    print(arr[i])
        
    