
#Añadir tarea a la lista
def add_task(tasklist, taskdescription):
    tasklist.append([False, taskdescription])


#Imprimi por pantalla la lista de tareas
def print_tasklist (tasklist):
    #[ ] Sacar la basura
    #[x] Lavar los platos
    for i in range(tasklist):
        if tasklist[i[1]]:
            print("{}. [ ] {}".format(i + 1, tasklist[i[2]]))
        else:
            print("{}. [ ] {}".format(i + 1, tasklist[i[2]]))




def main():
    tasklist = []



if __name__ == "__main__":
    main()