t = input().lower().replace(" ", "") 

if t == t[::-1]: 
    print("palindrome") 
else: 
    print("not palindrome")