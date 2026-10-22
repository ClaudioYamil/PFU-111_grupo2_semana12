# Menú interactivo: Diseña un bucle while que muestre un menú de opciones 
# y se repita de manera indefinida hasta que el usuario introduzca la opción de salir.
y = 0
z = 0
i = 0

def ye():
    ym = int(input("Introduce tu primer numero: \n"))
    return ym
    
    
def ze():
    zm = int(input("Introduce tu segundo numero: \n"))
    return zm
    
def ret():
    regresar = int(input("desea seguir operando?: \n1-sí\n2-no\n--"))
    if regresar <= 0 or regresar > 2:
        ("el valor que ah ingresado no se reconoce")
    elif regresar == 1:
        regresar = 0
        return regresar
    else:
        regresar = 1
        return regresar
        
while True:
    try:
        x = int(input("introduce una de las siguientes opciones:\n1-suma\n2-resta\n3-multiplicacion\n4-division\n5-salir\n--"))
        match x:
            case 1:
                while i != 1:
                    y = ye()
                    z = ze()
                    print(f"total : {y + z}")
                    i = ret()
                i = 0
            case 2:
                while i != 1:
                    y = ye()
                    z = ze()
                    print(f"total : {y - z}")
                    i = ret()
                i = 0
            case 3:
                while i != 1:
                    y = ye()
                    z = ze()
                    print(f"total : {y * z}")
                    i = ret()
                i = 0
            case 4:
                while i != 1:
                    y = ye()
                    z = ze()
                    print(f"total : {y / z}")   
                    i = ret()
                i = 0
            case 5:
                break
            case _:
                print("el numero que indrodujo no es valido\nvuelva a intentarlo\n")  
                  
    except:
        print("algo salio mal, vuelva a intenralo\n")    