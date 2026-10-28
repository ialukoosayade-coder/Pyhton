#meses c:
meses = ("enero", "febrero", "marzo", "abril", "mayo","junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
año = 2026
dia_semana = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
dia_meses = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

mes = 0
dia_semana_inicial = 3
print(meses[mes], año)

for nombre_dia in dia_semana:
    print(nombre_dia[:3], end=" ")
print()

for espacio in range(dia_semana_inicial):
    print("    ", end="")

for dia in range(1, dia_meses[mes] + 1):
    print(f"{dia:>3}", end=" ")

    if (dia_semana_inicial + dia) % 7 == 0:
        print()

print()

mes = 1
dia_semana_inicial2 = 6
print(meses[mes], año)

for nombre_dia in dia_semana:
   print(nombre_dia[:3], end=" ")
print()

for espacio in range(dia_semana_inicial2):
   print("    ", end="")

for dia in range(1, dia_meses[mes] + 1):
   print(f"{dia:>3}", end=" ")

   if(dia_semana_inicial2 + dia) % 7 == 0:
     print()

print()

mes = 2
dia_semana_inicial3 = 6
print(meses[mes], año)

for nombre_dia in dia_semana:
   print(nombre_dia[:3], end=" ")
print()

for espacio in range(dia_semana_inicial3):
   print("    ", end="")

for dia in range(1, dia_meses[mes] + 1):
    print(f"{dia:>3}", end=" ")
    if(dia_semana_inicial3 + dia) % 7 == 0:
      print()

print()

mes = 3
dia_semana_inicial4 = 2
print(meses[mes], año)

for nombre_dia in dia_semana:
   print(nombre_dia[:3], end=" ")
print()

for espacio in range(dia_semana_inicial4):
 print("    ", end="")

for dia in range(1, dia_meses[mes] + 1):
 print(f"{dia:>3}", end=" ")
 if(dia_semana_inicial4 + dia) % 7 == 0:
    print()
print() 