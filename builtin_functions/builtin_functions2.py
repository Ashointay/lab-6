t = input() 
upper_t= sum(map(str.isupper, t)) 
lower_t= sum(map(str.islower, t)) 

print("upper case letters:", upper_t) 
print("lower case letters:", lower_t)