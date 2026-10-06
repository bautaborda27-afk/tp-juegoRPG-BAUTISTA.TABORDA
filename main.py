from entidades import *
def menu ():
    print("1. Ver info (personaje)")
    print("2. Atacar Enemigo")
    print("3. Curar")
    print("4. Comprar arma")
    print("5. Comprar armadura")
    print("6. Comprar pociones")
    print("7. Salir")
    opc = int(input("Opcion: "))
    return opc
nombre = input("Ingresa el nombre de tu personaje: ")
personaje = crear_personaje(nombre)
while True:
    opc = menu()

    if opc == 1:
        mostrar_personje(personaje)
    elif opc == 2 :
        print("Quieres atacar 1vs1 o vas al puente de la muerte? responde: inv o puente")
        elec_batalla = input("- ")
        if elec_batalla.lower() == "inv":
            ganador, personaje = atacar_enemigo_inv(personaje)
            if ganador == 0:
                break
            elif ganador == 1:
                print("Felicitaciones ganaste")
                print("Ahora sigue con tu camino...")
                print()
            else:
                print("Algo huele a miedo...")
        elif elec_batalla.lower() == "puente":
            ganador,personaje = atacar_enemigo_pue(personaje)
            if ganador == 0:
                break
            elif ganador == 1:
                print("Felicitaciones ganaste")
                print("Ahora sigue con tu camino...")
                print()
    elif opc == 3:
        personaje = curar(personaje)
    elif opc == 4:
        print("")
        print("Estamos entrando a la tienda...")
        print
        personaje = comprar_arma(armas, personaje)

    elif opc == 5:
        print()
        print("Estamos entrando a la tienda...")
        print
        personaje = comprar_armaduras(personaje,armaduras)
    elif opc == 6:
        print()
        print("Estamos entrando a la tienda...")
        print
        personaje = comprar_pociones(personaje)
    elif opc == 7:
        print
        print
        print("Nos vemos fisura, no vuelvas...")
        break
        

        