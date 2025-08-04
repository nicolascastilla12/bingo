import random

def menu():
    entrada = input("Digite un número del 1 al 100 o 's' para salir: ").strip()
    
    if entrada.lower() == "s":
        print("Saliendo del programa...")
        return "s"
    
    if entrada.isdigit():
        entradaint = int(entrada)
        if 1 <= entradaint <= 100:
            return entrada
        else:
            print("¡Número fuera de rango!")
            return None
    else:
        print("¡Entrada inválida! Solo se aceptan números del 1 al 100 o 's' para salir.")
        return None

def jugar():
    entrada = 0
    contador = 1
    tarjeton = [0] * 11  # Índice 0 sin usar
    numeros_sorteados = set()
    aciertos = 0

    # Ingreso de números al cartón
    while entrada != "s" and contador <= 10:
        entrada = None
        while entrada is None:
            entrada = menu()
            if entrada == "s":
                break

        if entrada == "s":
            break

        entradaint = int(entrada)
        
        if entradaint in tarjeton:
            print("El valor ya se encuentra en el tarjetón:", entradaint)
        else:
            tarjeton[contador] = entradaint
            print("Se han ingresado", contador, "números al tarjetón.")
            contador += 1

    if contador > 1:
        print("\nTarjetón listo:", tarjeton[1:])
        print("¡Comienza el sorteo del bingo!\n")

        # Sorteo
        while aciertos < 10:
            if len(numeros_sorteados) == 100:
                print("¡Todos los números del 1 al 100 ya fueron sorteados y no se pudo completar el cartón!")
                break

            numero_sorteado = random.randint(1, 100)

            if numero_sorteado in numeros_sorteados:
                continue
            else:
                numeros_sorteados.add(numero_sorteado)
                print("Número sorteado:", numero_sorteado)

                if numero_sorteado in tarjeton:
                    aciertos += 1
                    print("¡Número acertado! Total de aciertos:", aciertos)
                else:
                    print("No está en el tarjetón.")

        if aciertos == 10:
            print("\n Partida terminada con éxito. ¡Se completaron los 10 aciertos del tarjetón!")
        else:
            print("\nFin del juego.")
    else:
        print("No se ingresaron números al tarjetón. El juego no puede comenzar.")
while True:
    jugar()
    reiniciar = input("\n¿Deseas jugar otra vez? (s/n): ").strip().lower()
    if reiniciar != "s":
        print("Gracias por jugar. ¡Hasta la próxima!")
        break