nums = [2,7,11,15]
target = 9

for n1 in nums:
    for n2 in nums:
        if n1 + n2 == target:
            print(f"{n1} + {n2} son los números necesarios")
        pass
