import actividad1
import actividad2
import actividad3

salida=False

while not salida:
    
    print("Pon el numero del juego al que deseas jugar")

    print ("1. Adivina el numero")

    print ("2. Piedra papel tijeras")

    print ("3. Ahorcado")

    print ("4. Salir del juego")
    
    seleccion_juego=int(input())
    
    if(seleccion_juego<=4):
        if (seleccion_juego==1):
            actividad1.numeros_random()

        elif (seleccion_juego==2):
            actividad2.Piedra_Papel_Tijeras()

        elif (seleccion_juego==3):
            actividad3.juegoAhorcado()

        elif (seleccion_juego==4):
            print("Adios, regresa pronto")
            salida=True
            
    else:
        print("Coloca un numero correctamente")
            
    