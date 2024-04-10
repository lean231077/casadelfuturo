import random

def jugar_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    
    while True:
        print("Juguemos a piedra, papel o tijeras!")
        jugada_usuario = input("Ingrese su jugada (piedra, papel o tijeras): ").lower()
        
        if jugada_usuario not in opciones:
            print("¡Jugada inválida! Por favor, ingrese piedra, papel o tijeras.")
            continue
        
        jugada_maquina = random.choice(opciones)
        
        print("La máquina elige:", jugada_maquina)
        
        if jugada_usuario == jugada_maquina:
            print("¡Empate!")
        elif (jugada_usuario == "piedra" and jugada_maquina == "tijeras") or \
             (jugada_usuario == "papel" and jugada_maquina == "piedra") or \
             (jugada_usuario == "tijeras" and jugada_maquina == "papel"):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")
        
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != "s":
            print("¡Gracias por jugar!")
            break

# Ejecutar el juego
jugar_piedra_papel_tijeras()