import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHİJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}();@#₺_&-+/*!?:.'"

total = lower + upper + numbers + symbols

password = random.choices(total, k=23)

password = ''.join(password)
print(password)