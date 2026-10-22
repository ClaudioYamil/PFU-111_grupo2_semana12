#Cálculo de factorial: Solicita un número entero positivo al usuario y calcula su factorial utilizando un contador y un bucle while.
while True:
    try:
        print("==== Factorial ====")
        n = int(input("introduce el numero al que quiere aplicarle factorial: \n"))
        contador = n
        r = 1
        if n > 0:
            while contador > 1:
                r *= contador
                contador -= 1
            print (r)
            break
        else:
            print("el numero no tiene que ser negativo\nvuelva a intentarlo")
            
    except:
        print("no has introducida nada aun o intentaste colocar caracteres\nintentalo de nuevo\n")