#Tabla de multiplicar: Dado un número entero, imprime su tabla de multiplicar del 1 al 10 utilizando un bucle for.
x = 1
while True:
    try:
        z = int(input("introduce un numero entero:\n"))
        for x in range(1, 11, 1):
            r = z * x
            print(f"{z} x {x} = {r}")
        break
            
    except:
        print("número invalido")