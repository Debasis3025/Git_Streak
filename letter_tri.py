word = "ramana"

for i in range(len(word)):
    s = ""
    for j in range(i + 1):
        s += word[j]
    print(s)