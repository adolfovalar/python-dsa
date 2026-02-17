"""
Problem: Two Sum
Time Complexity: O(n)
Space Complexity: O(n)
Objetivo: Debemos encontrar 2 números dentro de la lista nums que sumen 9
"""

nums = [2,7,11,15]
target = 9
vistos = {}

# Transformar lista en diccionario. El n1 será la clave. 
for index, n1 in enumerate(nums):
    #calcular número necesario
    num_necesario = target - n1
    print(f'El número necesario es {num_necesario}')
    #buscar número necesario en diccionario vistos
    if num_necesario in vistos:
        print(f'¡Se encontró el número necesario!')
        print(f'Los números que suman {target} son {n1} y {num_necesario}')
        break
    else:
        print(f'Todavía no hay ningún {num_necesario} en el diccionario')
        #Agremos número iterado a diccionario
        vistos[n1] = index
        print(f'El diccionario contiene{vistos}')


