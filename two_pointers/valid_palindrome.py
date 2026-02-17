frase = 'A man, a plan, a canal: Panama.'
frase_limpia = ''

# Limpiar la frase para eliminar signos y pasarlo a minúscula
for letra in frase:
    if letra.isalnum():
        frase_limpia += letra.lower()
print(f'La frase original es: {frase}')
print(f'La frase limpia es: {frase_limpia}')

l = 0
r = len(frase_limpia)-1

while l < r:
    if frase_limpia[l] == frase_limpia[r]:
        print(f'{frase_limpia[l]} y {frase_limpia[r]} son iguales.')
        l+=1
        r-=1 
    else:
        print('Son diferentes')
        break
    
    