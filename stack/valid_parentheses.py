s = '()[]{}'
stack = []
dict_caracteres = {')':'(', ']':'[','}':'{'}
es_valido = True 

for caracter in s:
    # CASO 1: Es de CIERRE (está en las llaves del diccionario)
    if caracter in dict_caracteres:
        # Verificamos si la pila tiene algo Y si hace pareja
        if len(stack) > 0 and dict_caracteres[caracter] == stack[-1]:
            stack.pop() 
            print(f"Se cerró: {caracter}. Stack actual: {stack}")
        else:
            # Si la pila estaba vacía O no era pareja -> ERROR
            print(f"Error detectado con: {caracter}")
            es_valido = False 
            break
            
    # CASO 2: Es de APERTURA
    else:
        stack.append(caracter)
        print(f"Se abrió: {caracter}. Stack actual: {stack}")

# AL FINAL:
# Debe ser válido (sin errores intermedios) Y la pila debe estar vacía
if es_valido and len(stack) == 0:
    print('¡ES VÁLIDO!')
else:
    print('NO ES VÁLIDO.')