import random

def obtener_eleccion_usuario():
    while True:
        eleccion = input("Elige piedra, papel o tijera: ").strip().lower()
        if eleccion in ["piedra", "papel", "tijera"]:
            return eleccion
        else:
            print("Entrada inválida. Por favor escribe piedra, papel o tijera.")

def obtener_eleccion_computadora():
    return random.choice(["piedra", "papel", "tijera"])

def determinar_resultado(usuario, computadora):
    if usuario == computadora:
        return "EMPATE"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        return "GANASTE"
    else:
        return "PERDISTE"

def jugar():
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    while True:
        usuario = obtener_eleccion_usuario()
        computadora = obtener_eleccion_computadora()
        print(f"Computadora eligió: {computadora}")
        resultado = determinar_resultado(usuario, computadora)
        print(f"Resultado: {resultado}")

        continuar = input("¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if continuar != 's':
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    jugar()
