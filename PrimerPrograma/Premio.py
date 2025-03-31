titulo = "El Juego de las cajas"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")
import random
numero_ganador = random.randint(1, 4)
print("Este juego se trata de encontrar el premio que esta escondido en 4 cajas.\n")
print("Tienes que ir eliminando cajas hasta llegar la correcta. \n")
print("Tienes las siguientes cajas: [1] [2] [3] [4] \n")
print("¿Qué caja quieres eliminar primero?. \n")
seleccion1=int(input("Selección:"))
print("\n")
if seleccion1 == 1 or seleccion1 == 2 or seleccion1 == 3 or seleccion1 == 4:
    if seleccion1 == numero_ganador:
        print("La caja [{}] conteía el tesoro.\n".format(seleccion1))
        print("Más suerte la proxima vez.\n")
        exit()
    else:
        print("La caja [{}] no conteía el tesoro.\n".format(seleccion1))
        print("¡SEGUIMOS JUGANDO!.\n")
        print("¡Te quedan tres cajas!.\n")
        if seleccion1 == 1:
            print("¿Qué cajas quieres eliminar ahora: [2] [3] [4]?. \n")
            seleccion2 = int(input("Selección:"))
            print("\n")
            if seleccion2 == 2:
                if seleccion2 == numero_ganador:
                    print("La caja [{}] conteía el tesoro.\n".format(seleccion2))
                    print("Más suerte la proxima vez.\n")
                    exit()
                else:
                    print("La caja [{}] no conteía el tesoro.\n".format(seleccion2))
                    print("¡SEGUIMOS JUGANDO!.")
                    print("¡Te quedan dos cajas!.\n")
                    print("¿Qué cajas crees que contiene el tesaoro la caja [3] o la [4]?. \n")
                    seleccion3 = int(input("Selección:"))
                    if seleccion3 == 3 or seleccion3 == 4:
                        if seleccion3 == numero_ganador:
                            print("La caja [{}] conteía el tesoro.\n".format(seleccion3))
                            print("Felicidades has conseguido el tesoro.\n")
                            exit()
                        else:
                            print("La caja [{}] no conteía el tesoro.\n".format(seleccion3))
                            print("Más suerte la proxima vez.")
                            exit()
                    else:
                        print("Opcion no valida")
                        exit()
            if seleccion2 == 3:
                if seleccion2 == numero_ganador:
                    print("La caja [{}] conteía el tesoro.\n".format(seleccion2))
                    print("Más suerte la proxima vez.\n")
                    exit()
                else:
                    print("La caja [{}] no conteía el tesoro.\n".format(seleccion2))
                    print("¡SEGUIMOS JUGANDO!.")
                    print("¡Te quedan dos cajas!.\n")
                    print("¿Qué cajas crees que contiene el tesaoro la caja [2] o la [4]?. \n")
                    seleccion3 = int(input("Selección:"))
                    if seleccion3 == 2 or seleccion3 == 4:
                        if seleccion3 == numero_ganador:
                            print("La caja [{}] conteía el tesoro.\n".format(seleccion3))
                            print("Felicidades has conseguido el tesoro.\n")
                            exit()
                        else:
                            print("La caja [{}] no conteía el tesoro.\n".format(seleccion3))
                            print("Más suerte la proxima vez.")
                            exit()
                    else:
                        print("Opcion no valida")
                        exit()
            if seleccion2 == 4:
                if seleccion2 == numero_ganador:
                    print("La caja [{}] conteía el tesoro.\n".format(seleccion2))
                    print("Más suerte la proxima vez.\n")
                    exit()
                else:
                    print("La caja [{}] no conteía el tesoro.\n".format(seleccion2))
                    print("¡SEGUIMOS JUGANDO!.")
                    print("¡Te quedan dos cajas!.\n")
                    print("¿Qué cajas crees que contiene el tesaoro la caja [2] o la [3]?. \n")
                    seleccion3 = int(input("Selección:"))
                    if seleccion3 == 2 or seleccion3 == 3:
                        if seleccion3 == numero_ganador:
                            print("La caja [{}] conteía el tesoro.\n".format(seleccion3))
                            print("Felicidades has conseguido el tesoro.\n")
                            exit()
                        else:
                            print("La caja [{}] no conteía el tesoro.\n".format(seleccion3))
                            print("Más suerte la proxima vez.")
                            exit()
                    else:
                        print("Opcion no valida")
                        exit()
            else:
                print("Opcion no valida")
                exit()
        elif seleccion1 == 2:
            if seleccion1 == 2:
                print("¿Qué cajas quieres eliminar ahora: [1] [3] [4]?. \n")
                seleccion2 = int(input("Selección:"))
                print("\n")
                if seleccion2 == 1:
                    if seleccion2 == numero_ganador:
                        print("La caja [{}] conteía el tesoro.\n".format(seleccion2))
                        print("Más suerte la proxima vez.\n")
                        exit()
                    else:
                        print("La caja [{}] no conteía el tesoro.\n".format(seleccion2))
                        print("¡SEGUIMOS JUGANDO!.")
                        print("¡Te quedan dos cajas!.\n")
                        print("¿Qué cajas crees que contiene el tesaoro la caja [3] o la [4]?. \n")
                        seleccion3 = int(input("Selección:"))
                        if seleccion3 == 3 or seleccion3 == 4:
                            if seleccion3 == numero_ganador:
                                print("La caja [{}] conteía el tesoro.\n".format(seleccion3))
                                print("Felicidades has conseguido el tesoro.\n")
                                exit()
                            else:
                                print("La caja [{}] no conteía el tesoro.\n".format(seleccion3))
                                print("Más suerte la proxima vez.")
                                exit()
                        else:
                            print("Opcion no valida")
                            exit()
                if seleccion2 == 3:
                    if seleccion2 == numero_ganador:
                        print("La caja [{}] conteía el tesoro.\n".format(seleccion2))
                        print("Más suerte la proxima vez.\n")
                        exit()
                    else:
                        print("La caja [{}] no conteía el tesoro.\n".format(seleccion2))
                        print("¡SEGUIMOS JUGANDO!.")
                        print("¡Te quedan dos cajas!.\n")
                        print("¿Qué cajas crees que contiene el tesaoro la caja [1] o la [4]?. \n")
                        seleccion3 = int(input("Selección:"))
                        if seleccion3 == 1 or seleccion3 == 4:
                            if seleccion3 == numero_ganador:
                                print("La caja [{}] conteía el tesoro.\n".format(seleccion3))
                                print("Felicidades has conseguido el tesoro.\n")
                                exit()
                            else:
                                print("La caja [{}] no conteía el tesoro.\n".format(seleccion3))
                                print("Más suerte la proxima vez.")
                                exit()
                        else:
                            print("Opcion no valida")
                            exit()
                if seleccion2 == 4:
                    if seleccion2 == numero_ganador:
                        print("La caja [{}] conteía el tesoro.\n".format(seleccion2))
                        print("Más suerte la proxima vez.\n")
                        exit()
                    else:
                        print("La caja [{}] no conteía el tesoro.\n".format(seleccion2))
                        print("¡SEGUIMOS JUGANDO!.")
                        print("¡Te quedan dos cajas!.\n")
                        print("¿Qué cajas crees que contiene el tesaoro la caja [1] o la [3]?. \n")
                        seleccion3 = int(input("Selección:"))
                        if seleccion3 == 1 or seleccion3 == 3:
                            if seleccion3 == numero_ganador:
                                print("La caja [{}] conteía el tesoro.\n".format(seleccion3))
                                print("Felicidades has conseguido el tesoro.\n")
                                exit()
                            else:
                                print("La caja [{}] no conteía el tesoro.\n".format(seleccion3))
                                print("Más suerte la proxima vez.")
                                exit()
                        else:
                            print("Opcion no valida")
                            exit()
                else:
                    print("Opcion no valida")
                    exit()
        elif seleccion1 == 3:
            print("¿Qué cajas quieres eliminar ahora: [1] [2] [4]?. \n")
            seleccion2 = int(input("Selección:"))
            print("\n")
            if seleccion2 == 1:
                if seleccion2 == numero_ganador:
                    print("La caja [{}] conteía el tesoro.\n".format(seleccion2))
                    print("Más suerte la proxima vez.\n")
                    exit()
                else:
                    print("La caja [{}] no conteía el tesoro.\n".format(seleccion2))
                    print("¡SEGUIMOS JUGANDO!.")
                    print("¡Te quedan dos cajas!.\n")
                    print("¿Qué cajas crees que contiene el tesaoro la caja [2] o la [4]?. \n")
                    seleccion3 = int(input("Selección:"))
                    if seleccion3 == 2 or seleccion3 == 4:
                        if seleccion3 == numero_ganador:
                            print("La caja [{}] conteía el tesoro.\n".format(seleccion3))
                            print("Felicidades has conseguido el tesoro.\n")
                            exit()
                        else:
                            print("La caja [{}] no conteía el tesoro.\n".format(seleccion3))
                            print("Más suerte la proxima vez.")
                            exit()
                    else:
                        print("Opcion no valida")
                        exit()
            if seleccion2 == 2:
                if seleccion2 == numero_ganador:
                    print("La caja [{}] conteía el tesoro.\n".format(seleccion2))
                    print("Más suerte la proxima vez.\n")
                    exit()
                else:
                    print("La caja [{}] no conteía el tesoro.\n".format(seleccion2))
                    print("¡SEGUIMOS JUGANDO!.")
                    print("¡Te quedan dos cajas!.\n")
                    print("¿Qué cajas crees que contiene el tesaoro la caja [1] o la [4]?. \n")
                    seleccion3 = int(input("Selección:"))
                    if seleccion3 == 1 or seleccion3 == 4:
                        if seleccion3 == numero_ganador:
                            print("La caja [{}] conteía el tesoro.\n".format(seleccion3))
                            print("Felicidades has conseguido el tesoro.\n")
                            exit()
                        else:
                            print("La caja [{}] no conteía el tesoro.\n".format(seleccion3))
                            print("Más suerte la proxima vez.")
                            exit()
                    else:
                        print("Opcion no valida")
                        exit()
            if seleccion2 == 4:
                if seleccion2 == numero_ganador:
                    print("La caja [{}] conteía el tesoro.\n".format(seleccion2))
                    print("Más suerte la proxima vez.\n")
                    exit()
                else:
                    print("La caja [{}] no conteía el tesoro.\n".format(seleccion2))
                    print("¡SEGUIMOS JUGANDO!.")
                    print("¡Te quedan dos cajas!.\n")
                    print("¿Qué cajas crees que contiene el tesaoro la caja [1] o la [2]?. \n")
                    seleccion3 = int(input("Selección:"))
                    if seleccion3 == 1 or seleccion3 == 2:
                        if seleccion3 == numero_ganador:
                            print("La caja [{}] conteía el tesoro.\n".format(seleccion3))
                            print("Felicidades has conseguido el tesoro.\n")
                            exit()
                        else:
                            print("La caja [{}] no conteía el tesoro.\n".format(seleccion3))
                            print("Más suerte la proxima vez.")
                            exit()
                    else:
                        print("Opcion no valida")
                        exit()
            else:
                print("Opcion no valida")
                exit()
        elif seleccion1 == 4:
            if seleccion1 == 4:
                print("¿Qué cajas quieres eliminar ahora: [1] [2] [3]?. \n")
                seleccion2 = int(input("Selección:"))
                print("\n")
                if seleccion2 == 1:
                    if seleccion2 == numero_ganador:
                        print("La caja [{}] conteía el tesoro.\n".format(seleccion2))
                        print("Más suerte la proxima vez.\n")
                        exit()
                    else:
                        print("La caja [{}] no conteía el tesoro.\n".format(seleccion2))
                        print("¡SEGUIMOS JUGANDO!.")
                        print("¡Te quedan dos cajas!.\n")
                        print("¿Qué cajas crees que contiene el tesaoro la caja [2] o la [3]?. \n")
                        seleccion3 = int(input("Selección:"))
                        if seleccion3 == 2 or seleccion3 == 3:
                            if seleccion3 == numero_ganador:
                                print("La caja [{}] conteía el tesoro.\n".format(seleccion3))
                                print("Felicidades has conseguido el tesoro.\n")
                                exit()
                            else:
                                print("La caja [{}] no conteía el tesoro.\n".format(seleccion3))
                                print("Más suerte la proxima vez.")
                                exit()
                        else:
                            print("Opcion no valida")
                            exit()
                if seleccion2 == 2:
                    if seleccion2 == numero_ganador:
                        print("La caja [{}] conteía el tesoro.\n".format(seleccion2))
                        print("Más suerte la proxima vez.\n")
                        exit()
                    else:
                        print("La caja [{}] no conteía el tesoro.\n".format(seleccion2))
                        print("¡SEGUIMOS JUGANDO!.")
                        print("¡Te quedan dos cajas!.\n")
                        print("¿Qué cajas crees que contiene el tesaoro la caja [1] o la [3]?. \n")
                        seleccion3 = int(input("Selección:"))
                        if seleccion3 == 1 or seleccion3 == 3:
                            if seleccion3 == numero_ganador:
                                print("La caja [{}] conteía el tesoro.\n".format(seleccion3))
                                print("Felicidades has conseguido el tesoro.\n")
                                exit()
                            else:
                                print("La caja [{}] no conteía el tesoro.\n".format(seleccion3))
                                print("Más suerte la proxima vez.")
                                exit()
                        else:
                            print("Opcion no valida")
                            exit()
                if seleccion2 == 3:
                    if seleccion2 == numero_ganador:
                        print("La caja [{}] conteía el tesoro.\n".format(seleccion2))
                        print("Más suerte la proxima vez.\n")
                        exit()
                    else:
                        print("La caja [{}] no conteía el tesoro.\n".format(seleccion2))
                        print("¡SEGUIMOS JUGANDO!.")
                        print("¡Te quedan dos cajas!.\n")
                        print("¿Qué cajas crees que contiene el tesaoro la caja [1] o la [2]?. \n")
                        seleccion3 = int(input("Selección:"))
                        if seleccion3 == 1 or seleccion3 == 2:
                            if seleccion3 == numero_ganador:
                                print("La caja [{}] conteía el tesoro.\n".format(seleccion3))
                                print("Felicidades has conseguido el tesoro.\n")
                                exit()
                            else:
                                print("La caja [{}] no conteía el tesoro.\n".format(seleccion3))
                                print("Más suerte la proxima vez.")
                                exit()
                        else:
                            print("Opcion no valida")
                            exit()
                else:
                    print("Opcion no valida")
                    exit()
        else:
            print("Opcion no valida")
            exit()
else:
    print("Opcion no valida")
    exit()










