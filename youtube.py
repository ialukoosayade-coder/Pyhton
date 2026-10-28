datos = [4, 7, 2]
total = 0
contador = 0

for numero in datos:
    while contador < 2:
        if numero > 3 or numero == 2:
            total = total + numero
        else:
            total = total - 1

        contador = contador + 1

print(total)
print(contador)