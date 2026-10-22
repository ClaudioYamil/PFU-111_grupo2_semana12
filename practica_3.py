#Recorrer una cadena: Pide al usuario una palabra e imprime cada letra de esta en una línea independiente.
while True:
    try:
        name = str(input("introduce tu nombre:\n")).strip()
        
        if name:
            for i in name:
                print(i)
                
            break
        else:
            print("nombre vacion\n")
    except ValueError:
        print("no pusiste tu nombre aun bro")