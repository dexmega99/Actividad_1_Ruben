import random

#JUEGO DEL AHORCADO

def juegoAhorcado():

    #Abrimos el fichero donde tendra las palabras
    with open("juego_penjat.txt","r") as file:
        alltext=file.read()
        words = list(map(str, alltext.split()))

    #Escogemos una de las palabras de forma aleatoria
    palabra_random=random.choice(words)
    
    #Contamos el numero de letras para despues hacer que escriba diferentes _
    numero_letras=len(palabra_random)
    
    palabra_sin_descubrir= numero_letras * "_" 
    
    #Contador de intentos 
    contador_intentos=numero_letras*2
    
    salir = False
    
    print(palabra_sin_descubrir)

    lista=list(palabra_sin_descubrir)
    count=0
    
    #Creamos un bucle para seguir  jugando hasta quedarnos sin intentos
    while contador_intentos>0 and not salir:
        letra=input("Selecciona la letra que crees que esta")
        count=0
        
        #Hacemos un for para que recorra cada letra de la palabra, si la letra que indicamos es correcta la escribira    
        for i in palabra_random:
            if(i==letra):
                lista[count]=letra
                palabra_sin_descubrir="".join(lista)
            
            count=count +1
        print(palabra_sin_descubrir)    
        contador_intentos=contador_intentos-1
    
        if("_" not in palabra_sin_descubrir and contador_intentos>0):
            print("Has ganado \n")
            salir=True
            
    if(contador_intentos==0):
        print("Has perdido \n")
        