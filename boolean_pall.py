def bool_pall(s):
    if s == s[::-1]:
        #print("The string is a palindrome")
        return True
    else:
        #print("The string is not a palindrome")
        return False


bl=bool(bool_pall("mam"))
print(bl)   

 
