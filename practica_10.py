#Suma hasta número negativo: Pide números al usuario de forma repetida hasta que introduzca un número negativo
# , momento en el cual el bucle terminará y mostrará la suma acumulada de los valores ingresados.
def suma():
    sum = int(input("introduce un numero hasta uno negativo:\n"))
    return sum

while True:
    try:
        r = 0
        s = suma()
        while s > 0:
            r += s
            s = suma()
        print(r)
        break
    except:
        print("no se admite letras u caracteres")