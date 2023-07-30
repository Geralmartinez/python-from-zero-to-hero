#separar la lista en 3 lista una con los números pares y otra con los inpares y calcular su promedio
numbers = [14,52,54,64,76,23,5,2,54,6,32]
even = []
odds = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
        else:
            odds.append(num)
even_sum = 0
for
