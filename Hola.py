edad = int(input("cuantos años tienes?"))

alumno = input("Eres alumno del centro? (True/False): ")
inscrito = input("¿Estás inscrito al centro? (True/False): ")
sancionado = input("¿Estás sancionado? (True/False): ")

if (alumno == "True" or inscrito == "True" or " edad <=16 and edad >= 25" == "True" ) and sancionado == "False":
 print("puede acceder")
else:
 print("no puede acceder")


