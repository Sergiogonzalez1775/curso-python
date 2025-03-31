import os
import random

BODY_PARTS = ["Pecho","Pierna","Espalda","Bíceps","Tríceps","Hombro"]

EXERCISES = {
    "Pecho":["Press banca, 4x12",
             "Press inclinado con mancuernas, 3x12",
             "Press martillo en banco inclinado con mancuernas, 3x12",
             "Aperturas en banco inclinado, 3x10",
             "Press de banca declinado alternado con mancuernas, 3x12",
             "Flexiones, 4x10"],

    "Pierna":["Sentadilla, 4x10",
              "Sentadilla sumo con pesa rusa, 4x10",
              "Sentadilla split con mancuernas, 4x10",
              "Sentadilla split con barra, 4x10",
              "Sentadillas con salto, 4x12",
              "Sentadilla búlgara, 3x10"],

    "Espalda":["Remo supino con mancuernas, 4x10",
              "Remo sentado con banda elástica, 4x10",
              "Remo inclinado en banco con mancuernas (agarre prono), 4x10",
              "Remo con banda elástica (de pie), 4x10",
              "Remo al cuello con banda elástica, 4x10"],

    "Bíceps":["Curl con barra, 4x10",
              "Curl alternado con banda elástica, 3x10",
              "Curl agarre prono con mancuernas, 3x10",
              "Curl invertido con barra, 4x10",
              "Curl martillo con mancuernas, 3x10"],

    "Tríceps":["Press de copa con mancuerna de pie, 4x10",
              "Patada de tríceps con banda elástica, 3x10",
              "Flexiones sobre los antebrazos, 4x10",
              "Extensión de tríceps acostado con mancuerna, 3x10",
              "Extensión mancuerna tras nuca con una mano (de pie), 3x10"],

    "Hombro":["Press militar con barra (agarre abierto), 4x10",
              "Press de hombros sentado con mancuernas (agarre neutro), 4x10",
              "Press Arnold con mancuernas, 4x10",
              "Elevaciones frontales con barra, 4x10",
              "Elevaciones laterales con mancuernas, 4x10"]
}

WARM_UP = {
    "Calentamiento":["Movilidad cuerpo","Movilidad pierna","Bicicleta"],
    "Estiramientos":["Rutina general de estiramientos"]
}

#function to clear the terminal and wait for an enter
def clear_and_continue():
    input("Enter para continuar...\n\n")
    os.system("clear")


#function that ask preferences to the user
def ask_user_preferences():
    print("Crearemos un entrenamiento basado en tus preferencias")
    clear_and_continue()

    num_days = 0

    #numer of trainig days input
    while 2 > num_days < 6:
        try:
            num_days = int(input("¿Cuantos dias vas a entrenar?"))
            if 2 > num_days < 6:
                print("Los dias deben ser minimo 2 y maximo 5")
        except ValueError:
            print("Solo valores numericos entre 2 y 5 incluidos")
    clear_and_continue()

    time = 0

    #mins of trainig per days input
    while time < 50:
        try:
            time = int(input("¿Cuanto tiempo tienes para entrenar?"))
            if time < 50:
                print("Debes tener un minimo de 50min por día")

        except ValueError:
            print("Solo valores numericos mayores a 50")

    return time, num_days


#fuction that generate the training plan
def gen_training_plan(time, num_days):

    training_plan = {}

    #create the training plan structure
    for i in range(0, num_days):
        training_plan["DAY " + str(i + 1)] = {"boddy_part": [], "exercises": [], }

    body_parts = ["Pecho", "Pierna", "Espalda", "Bíceps", "Tríceps", "Hombro"]


    #dive the boddy parts per days
    while len(body_parts) > 0:
        for day in training_plan:
            try:
                body_part = random.choice(body_parts)
                training_plan[day]["boddy_part"].append(body_part)
                body_parts.remove(body_part)

            except IndexError:
                break

    #add warm up
    for day in training_plan:
        training_plan[day]["exercises"].append(random.choice(WARM_UP["Calentamiento"]))
        training_plan[day]["exercises"].append(random.choice(WARM_UP["Estiramientos"]))
    time -= 10


    #select the exercises for the day per boddy part assigned
    for day in training_plan:
        day_time = time
        while day_time > 0:
            for part in training_plan[day]["boddy_part"]:
                if day_time > 0:
                    training_plan[day]["exercises"].append(random.choice(EXERCISES[part]))
                    day_time -= 5
                else:
                    continue

    return training_plan


#Fuction that impress the plan
def show_plan(training_plan):
    print("Este es tu plan personalizado de entrenamiento:\n")

    num = 1

    for day in training_plan:
        print("------------ DAY"+ str(num) + " ------------")
        for exercise in training_plan[day]["exercises"]:
            print(exercise)
        num +=1
        print("\n")


def main():
    print("Bievenido al programa de entrenamiento")
    clear_and_continue()

    time, num_days = ask_user_preferences()

    training_plan = gen_training_plan(time, num_days)

    os.system("clear")

    show_plan(training_plan)


if __name__ == "__main__":
    main()