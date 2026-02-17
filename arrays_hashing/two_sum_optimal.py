nums = [2,7,11,15]
target = 9
vistos = {}

for index, n1 in enumerate(nums):
    num_necesario = target - n1
    print(f'el número necesario es {num_necesario}')

    if num_necesario in vistos:
        print(f'los números son {n1} y {num_necesario}')
        break


