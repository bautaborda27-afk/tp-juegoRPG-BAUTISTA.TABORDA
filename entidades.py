import random 
vida_max = 100
armas= {
    "mano":{
        "nombre":"mano",
        "dolor":30,
        "golpe_critico":200,
        "precio":0
    },
    "espada":{
        "nombre":"espada",
        "dolor":50,
        "golpe_critico":300,
        "precio":1000
    },
    "la_mano_de_D10S":{
        "nombre":"la_mano_de_D10S",
        "dolor":70,
        "golpe_critico":100000,
        "precio":1000000000
    }
}
armaduras = {
    "sabana":{
        "nombre":"sabana",
        "resistencia":0,
        "precio":0

    },
    "barril_chavo":{
        "nombre":"barril_chavo",
        "resistencia":8,
        "precio":808
    },
    "telgopor":{
        "nombre":"telgopor",
        "resistencia":50,
        "precio":2000
    }
}



enemigos={
    "0":{
        "nombre":"Fisura",
        "vida":40,
        "dolor":30,
        "tesoro":-1
    },
    "1":{
        "nombre":"Bostero",
            "vida":50,
            "dolor":15,
            "tesoro":18
        },
    "2":{
            "nombre":"Millo",
            "vida":100,
            "dolor":30,
            "tesoro":200
        }
}


personaje_principal = {
    "nombre":"",
    "vida":vida_max,
    "vida_max": vida_max,
    "fuerza":0,
    "suerte":0,
    "monedas":0,
    "pociones":0,
    "arma":armas["mano"],
    "armadura":armaduras["sabana"]
}


def crear_personaje (nombre):
    global personaje_principal
    personaje = personaje_principal.copy()

    personaje["nombre"] = nombre
    personaje["fuerza"] = random.randint(0,101)
    personaje["suerte"] = random.randint(0,100)

    return personaje

def mostrar_personje(personaje:dict):
    print("Nombre:", personaje["nombre"])
    print("Vida: ", personaje["vida"],"/",personaje["vida_max"])
    print("Fuerza: ", personaje["fuerza"])
    print("Suerte: ", personaje["suerte"])
    print("Monedas: ", personaje["monedas"])
    print("Pociones: ", personaje["pociones"])
    print("Arma: ", personaje["arma"]["nombre"], "---  Daño: ", personaje["arma"]["dolor"])
    print("Armadura: ", personaje["armadura"]["nombre"], "---  Resistencia: ", personaje["armadura"]["resistencia"])

def comprar_arma (armas:dict, personaje:dict):
    print ("Armas que podes comprar: ")
    print("1. ", "Nombre: ", armas["espada"]["nombre"])
    print("   ", "Daño: ", armas["espada"]["dolor"])
    print("   ", "Golpe critica:", armas["espada"]["golpe_critico"])
    print("   ", "Precio:", armas["espada"]["precio"])
    print()
    print()
    print("2. ", "Nombre: ", armas["la_mano_de_D10S"]["nombre"])
    print("   ", "Daño: ", armas["la_mano_de_D10S"]["dolor"])
    print("   ", "Golpe critica:", armas["la_mano_de_D10S"]["golpe_critico"])
    print("   ", "Precio:", armas["la_mano_de_D10S"]["precio"])
    print()
    elec = int(input("OPC: "))
    if elec == 1:
        if personaje["monedas"] >= armas["espada"]["precio"]:
            personaje["monedas"] -= armas["espada"]["precio"]
            personaje["arma"] = armas["espada"]
        else: 
            print("Pobre de mierda, no te alcanza la money")
    elif elec == 2:
        if personaje["monedas"] >= armas["la_mano_de_D10S"]["precio"]:
            personaje["monedas"] -= armas["la_mano_de_D10S"]["precio"]
            personaje["arma"] = armas["la_mano_de_D10S"]    
        else: 
            print("Pobre de mierda, no te alcanza la money")
    return personaje

def comprar_armaduras(personaje:dict, armaduras:dict):
    print ("Armaduras que podes comprar: ")
    print("1. ", "Nombre: ", armaduras["barril_chavo"]["nombre"])
    print("   ", "Resistencia:", armaduras["barril_chavo"]["resistencia"])
    print("   ", "Precio:", armaduras["barril_chavo"]["precio"])
    print()
    print()
    print("2. ", "Nombre: ", armaduras["telgopor"]["nombre"])
    print("   ", "Resistencia:", armaduras["telgopor"]["resistencia"])
    print("   ", "Precio:", armaduras["telgopor"]["precio"])
    print()
    elec = int(input("OPC(1~2): "))
    if elec == 1:
        if personaje["monedas"] >= armaduras["barril_chavo"]["precio"]:
            personaje["monedas"] -= armaduras["barril_chavo"]["precio"]
            personaje["armadura"] = armaduras["barril_chavo"]
            print()
            print("Se te entrego el arma, haber si asi le ganas a alguien")
        else: 
            print("Pobre de mierda, no te alcanza la money")
    elif elec == 2:
        if personaje["monedas"] >= armaduras["telgopor"]["precio"]:
            personaje["monedas"] -= armaduras["telgopor"]["precio"]
            personaje["armadura"] = armaduras["telgopor"]
            print()
            print("Ahora estas un poco protegido ~")
        else: 
            print("Pobre de mierda, no te alcanza la money")
    return personaje    

def comprar_pociones(personaje):
    print("Las pociones salen 150, voy a revisar tus fondos...")
    if personaje["monedas"] >= 150:
        print ("Toma el elixir, no eras tan pobre como parecias")
        personaje["monedas"] -= 150
        personaje["pociones"] += 1
        return personaje
    else:
        print("Sali de acá, sos un quebrado asi que vola")
        return personaje
    
def atacar_enemigo_inv (personaje):
    enemigo = random.randint(0,2)
    if enemigo == 0:
        enemigo = enemigos["0"].copy()
    elif enemigo == 1:
        enemigo = enemigos["1"].copy()
    else :
        enemigo = enemigos["2"].copy()
    print ("Te esta atacando: ", enemigo["nombre"])
    print()
    print()
    print("Lo atacas? si o no ")
    atacar_anwser = input("- ")
    if atacar_anwser.lower() == "si":
        while True:
            dolor = personaje["arma"]["dolor"]
            enemigo["vida"] -= dolor*(personaje["suerte"]/3)
            if enemigo["vida"] < 0:
                print("EL ENEMIGO MURIO")
                personaje["monedas"] += enemigo["tesoro"]
                return 1, personaje
            personaje["vida"] -= enemigo["dolor"]
            if personaje["vida"] <= 0:
                    print("Perdiste, JAJAJA re bobo")
                    return 0, personaje
            print("Tu vida: ",personaje["vida"])
            print("Enemigo vida: ",enemigo["vida"])
            print("----------------------------")
            input("Presione enter para la siguiente ronda..")
    else:
        return 5, personaje


def atacar_enemigo_pue(personaje):
    print()
    print("No creo que haya sido la opcion correcta...")
    print()
    print("Estoy preparando el puente")
    cant_enemigos = random.randint(1,50)
    puente = []
    for i in range(cant_enemigos):
        enemigo = random.randint(0,2)
        if enemigo == 0:
            enemigo = enemigos["0"]
        elif enemigo == 1:
            enemigo = enemigos["1"]
        else :
            enemigo = enemigos["2"]
        puente.append(enemigo.copy())

    for enemigo in puente:
            print("Peleas con ", enemigo["nombre"])
            while enemigo["vida"] > 0 and personaje["vida"] > 0:
                dolor = personaje["arma"]["dolor"]
                enemigo["vida"] -= dolor*(personaje["suerte"]/3)
                if enemigo["vida"] < 0:
                    print("EL ENEMIGO MURIO")
                    personaje["monedas"] += enemigo["tesoro"]
                else:
                    personaje["vida"] -= enemigo["dolor"]
                if personaje["vida"] <= 0:
                    print("Perdiste, JAJAJA re bobo")
                    return 0, personaje
                print(personaje["vida"])
                print(enemigo["vida"])
                input("Presione enter para la siguiente ronda..")

    print("TERMINO EL PUENTE")
    personaje["monedas"] += 100
    return 1, personaje
    
    
def curar (personaje):
    curacion_disponible = personaje["pociones"]
    if curacion_disponible <= 0:
        print("No tienes vida disponible...")
        return personaje
    else:
        print("Curando...")
        personaje["pociones"] -= 1
        personaje["vida"] = 100
        return personaje

