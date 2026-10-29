print("--- Bienvenido al calculador de notas ---")

contador_de_notas = 1
cantidad_de_notas_aprobadas = 0 
cantidad_de_notas_desaprobadas = 0
promedio_de_notas_aprobadas = 0.0
promedio_de_notas_desaprobadas = 0.0
promedio_de_notas_total = 0.0
nota_actual = 0.0





cantidad_total_de_notas = int(input("Ingrese la cantidad de Notas: "))
print (cantidad_total_de_notas)

while contador_de_notas <= cantidad_total_de_notas:
    print  ("Ingrese la nota numero: ", contador_de_notas )
    nota_actual = int(input("Nota: " ))
    if nota_actual < 70:
            cantidad_de_notas_desaprobadas = cantidad_de_notas_desaprobadas + 1
            promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas + nota_actual
    elif nota_actual >= 70:
            cantidad_de_notas_aprobadas = cantidad_de_notas_aprobadas + 1
            promedio_de_notas_aprobadas = promedio_de_notas_aprobadas + nota_actual
            promedio_de_notas_total = promedio_de_notas_total + (nota_actual /cantidad_total_de_notas)
    contador_de_notas = contador_de_notas + 1

if cantidad_de_notas_desaprobadas > 0:
        promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas / cantidad_de_notas_desaprobadas
else:
    cantidad_de_notas_desaprobadas = 0

if cantidad_de_notas_aprobadas > 0: 
    promedio_de_notas_aprobadas = promedio_de_notas_aprobadas / cantidad_de_notas_aprobadas
else:
    cantidad_de_notas_aprobadas = 0

print ("El estudiante tiene esta cantidad de notas aprobadas ", cantidad_de_notas_aprobadas)
print ("Este es el promedio de notas aprobadas ", promedio_de_notas_aprobadas)
print ("El estudiante tiene esta cantidad de notas desaprobadas ", cantidad_de_notas_desaprobadas)
print ("Este es el promedio de notas aprobadas ", promedio_de_notas_desaprobadas)
print ("Este es el promedio de notas Total ", promedio_de_notas_total)

