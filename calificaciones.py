calificaciones = [45, 80, 90, 70, 55, 100, 60, 40, 85, 75]
lista_aprovados = []
lista_reprovados = []
promedio = sum(calificaciones) / len(calificaciones)
alta = max(calificaciones)
baja = min(calificaciones)

for i in calificaciones:
    if i >= 60:
        lista_aprovados.append(i)
    else:
        lista_reprovados.append(i)

print("Promedio:", promedio)
print("Calificación más alta:", alta)
print("Calificación más baja:", baja)
print("Aprobados:", lista_aprovados)
print("Reprobados:", lista_reprovados)
print("Número de aprobados:", len(lista_aprovados))
print("Número de reprobados:", len(lista_reprovados))
