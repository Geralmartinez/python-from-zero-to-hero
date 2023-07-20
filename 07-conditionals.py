# la ejecución condicional de código se realiza evaluando sentencia lógicas.estas sentencias entregan un valor de tipo booleano (bool),es decir entregan true o false

print("-----------expreciones booleanas")
print(5>4)
print(5<4)
print(4 == '4')
print(4 != 4)
# si queremos comparar menor o igual
print(4 <= 4)
#para mayor o igual 
print(4 >= 4)

#podemos tanbién tener expreciones booleanas compuestas utilizando los operadores and, or y not 
print("--------------expreciones booleanas compuestas-----------")
print(4 < 5 or 6 > 8)#tru or false => true
print(4 < 5 and 6 > 8)#true and false => false
print(4 > 5 and 6 > 8)#false and false => false

print(not true)
print(not false)