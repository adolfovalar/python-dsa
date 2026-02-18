s = '())[]{}'
stack = []
dict_caracteres = {')':'(', ']':'[','}':'{'}

# Guardar carácteres en el stack.
for caracter in s:
    if caracter in dict_caracteres and len(stack) > 0:
        if dict_caracteres[caracter] == stack[-1]:
            stack.pop()
            print(stack)
        else: 
            break
    else:
        stack.append(caracter)
        print(stack)

if len(stack) > 0:
    print('No es válido.')


