from functools import reduce 
import operator 

n = list(map(int, input().split()))
print(reduce(operator.mul, n, 1))