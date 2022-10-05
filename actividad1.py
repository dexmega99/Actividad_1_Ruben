from random import randrange

#JUEGO NUMERO RANDOM

def numeros_random():
    
    #Contador intentos
    contador_intentos=0

    #utilizamos randrange para generar un numero aleatorio del 1 al 10
    adivinar= randrange(10)

    #Generamos un bluce que no para hasta que te quedes sin intentos o bien hayas acertado el numero
    while contador_intentos < 3:
        
        numero=int(input("Introduce un numero del 1 al 10 "))
        
        if(numero==adivinar):
            print("Has ganado \n")
            contador_intentos=3

        elif(numero!=adivinar):
            print("No has acertado")
            
            
        contador_intentos= contador_intentos+1
        
    if (contador_intentos==3):   
        print("has perdido, el numero correcto era el ", adivinar ,"\n")

