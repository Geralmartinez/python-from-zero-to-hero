import time

#hacer un programa que cuente regresivamente desde 10 y cuando al llegar a cero diga "boom"
#10
#9
#8
#...
#boom

num = 10
while (num >= 0):
    print(num)
    time.sleep(1)
    num = num -1
print("!!boom¡¡")