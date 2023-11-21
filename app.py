#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random

from flask import Flask
app = Flask(__name__)

from flask import request
@app.route("/jugar", methods=["POST"])

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# lista de opciones juego papel, tijera, piedra
opciones = ["rock", "paper", "scissors"]

# inicializa una variable de puntuacion
puntuacion = 0

# inicializa una variable rondas
rondas = 0

def jugar():
    global puntuacion
    global rondas

    rondas += 1

    # pide al usuario por consola que elija una opcion y transforma a minusculas
    eleccion = input("Elige rock, paper o scissors: ").lower()

    # si el usuario escribe algo diferente a piedra, papel o tijera se lo hacemos saber
    if eleccion not in opciones:
        print("Escribe una de las opciones correctas!")
        return jugar()
    
    # crea la logica del juego
    computadora = random.choice(opciones)
    if eleccion == computadora:
        print("Empate!")
    elif eleccion == "rock" and computadora == "scissors":
        print("Ganaste!")
        puntuacion += 1
    elif eleccion == "paper" and computadora == "rock":
        print("Ganaste!")
        puntuacion += 1
    elif eleccion == "scissors" and computadora == "paper":
        print("Ganaste!")
        puntuacion += 1
    else:
        print("Perdiste!")
        puntuacion -= 1

    # pide al usuario si quiere jugar de nuevo
    jugar_de_nuevo = input("Quieres jugar de nuevo? (si/no): ").lower()

    # mostrar puntuacion usuario si elige no
    if jugar_de_nuevo == "no":
        print("Tu puntuacion final es: " + str(puntuacion))
        print("Has jugado un total de: " + str(rondas) + " rondas")
    elif jugar_de_nuevo == "si":
        jugar()
    else:
        print("Escribe si o no")
        return jugar()

jugar()