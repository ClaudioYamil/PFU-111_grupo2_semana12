#Números pares del 1 al 20: Utiliza un bucle while para imprimir todos los números pares comprendidos entre el 1 y el 20.
x = 0

while x <= 20 :
    x += 1
    par = x%2
    if par == 0:
        print(x)
        