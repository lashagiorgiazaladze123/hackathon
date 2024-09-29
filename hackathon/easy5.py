def didi(n, y):
    if n > 1:
        x = y % n
    if x != 0:
        return "არ იყოფა"
    else:
        return y // n

print(didi(4, 45))