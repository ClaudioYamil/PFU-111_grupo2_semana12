#Adivinar el número: Crea un programa con un número secreto fijo; el bucle 
#while debe pedir intentos al usuario e indicarle si el número secreto es mayor o menor hasta que acierte.
Clave = 679
i = 0
while True:
    try:
        print("==ADIVINAD LA CLAVE")
        log = int(input("Introduce la clave que crees correcta: \n"))
        if log != Clave:
            print("no le has atinado!\n")
            while i != 1:
                if log < Clave:
                    print(f"la clave es mayor que {log}")
                    log = int(input("intentalo de nuevo\n"))
                elif log > Clave:
                    print(f"la clave es menor que {log}")
                    log = int(input("intentalo de nuevo\n"))
                else:
                    print("ya atinaste la clave")
                    i = 1
            
        break
    except:
        print("error al no indroducir nada")