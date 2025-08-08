a=[2,7,11,15]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==9:
            print("Indices of the numbers that add up to 9 are:", i, j)
            break
    else:
        continue
    