import random

#Juego Piedra Papel Tijeras

def Piedra_Papel_Tijeras():

    #Creamos dos variables que seran los puntos del jugador y de la maquina
    puntos_jugador=0
    puntos_maquina=0

    #Las jugadas de la maquina estaran dentro de una lista
    jugada_maquina=['piedra', 'papel', 'tijeras']

    #Generamos un bucle while que no para hasta que uno de los dos gane
    while puntos_jugador <3 and puntos_maquina<3:
        
        jugada_jugador=str(input("¿Que utilizaras? Piedra, papel, tijeras ")).lower()
        
        #Escogemos de forma aleatoria el movimiento de la maquina
        resultado_maquina=random.choice(jugada_maquina)
        
        #Comrpueba si han empatado
        if(jugada_jugador == resultado_maquina):
            print("empate, el jugador tiene ", puntos_jugador, " y la maquina tiene", puntos_maquina)

        #Comprueba si gana usando tijeras
        elif(jugada_jugador=="tijeras" and resultado_maquina=="papel"):
            puntos_jugador=puntos_jugador+1
            print("has ganado la ronda, el jugador tiene ", puntos_jugador, " y la maquina tiene", puntos_maquina)
            
        #Comprueba si gana usando papel    
        elif(jugada_jugador=="papel" and resultado_maquina=="piedra"):
            puntos_jugador=puntos_jugador+1
            print("has ganado la ronda, el jugador tiene ",puntos_jugador, " y la maquina tiene", puntos_maquina)
            
        #Comprueba si gana usando piedra    
        elif(jugada_jugador=="piedra" and resultado_maquina=="tijeras"):
            puntos_jugador=puntos_jugador+1
            print("has ganado la ronda, el jugador tiene ", puntos_jugador, " y la maquina tiene", puntos_maquina)
        
        #Comprueba si pierde   
        else:
            puntos_maquina=puntos_maquina+1
            print("has perdido la ronda, el jugador tiene ", puntos_jugador, " y la maquina tiene", puntos_maquina)
            print(resultado_maquina)

    if(puntos_jugador==3):
        print("HAS GANADO ERES EL MEJOR \n")
    elif(puntos_maquina==3):
        print("TE GANO LA MAQUINA \n")
        
