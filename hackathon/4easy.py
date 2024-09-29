def luwebi(nums):
    listn = []
    for i in nums:
        if i % 2 == 0:
            listn.append(i)
    return listn


print(luwebi([5, 4, 56, 7, 8, 3, 563]))