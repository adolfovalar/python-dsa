"""
PROBLEM: Contains Duplicate
Time Complexity: O(n)
Space Complexity: O(n)
Objetivo: Dada una lista de números, devuelve True si algún valor aparece al menos dos veces y False si todos son únicos. 
"""

nums = [1,1,2,3,3]
nums_set = set()


for n in nums:
    if n in nums_set:
        print(f'{n} está repetido')
        break
    #si no está lo agregamos
    else:
        nums_set.add(n)



