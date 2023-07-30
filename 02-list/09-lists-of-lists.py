#podemos tener listas anidadas:

#podríamos tener unas lista con las calificaciones de cada estiadentes

students = ["seba", "gonza", "gaby"]
grades = [[5,6,4,5,6,7],[6,7,6,5,6,4],[6,6,5,6,7,7]]

#se puede hacer un programa que imprima algo similar a:
#El estudiante seba tiene un promedio xx
#El estudiante gonza tiene un promedio yy
#El estudiante gaby tiene un promedio zz
averages = []
for students_grades in grades:
    averages.append(sum(students_grades)/len(students_grades))

for position in range(len(students)):
    print("El estudiante",students(position),"tiene promedio",average(position))