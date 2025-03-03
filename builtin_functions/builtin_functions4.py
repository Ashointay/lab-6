n = int(input())
ms = int(input())
from time import sleep

sleep(ms / 1000)
result = n ** 0.5  # Вместо math.sqrt()

print("Square root of", n, "after", ms, "milliseconds is", result)
