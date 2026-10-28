punts = 0
comptador = 0
for i in range(1, 4):      
    for j in range(1, 4):
        if i == j:
            punts = punts + 2
        else:
            if i > j:
                punts = punts + 1
            else:
                comptador = comptador + 1

print(punts)
print(comptador)
