#Contar vocales: Recorre una frase ingresada por el usuario y cuenta cuántas vocales contiene en total.Ejercicios con bucle while
while True:
    try:
        word = str(input("Introduce algo:\n")).strip()
        lin = len(word)
        x = 0
        vocal = "aeiouAEIOU"
        valor = 0
        if word:
            while valor < lin:
                if word[valor] in vocal:
                    x +=1
                valor += 1 
            print(f"la cantidad de vocales es: {x}")
            break
        else:
            print("no has introducido algo")
    except:
        print("algo invalido :V\nvuelve a intentarlo\n")
     
    

