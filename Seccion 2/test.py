#pisos = 10;print(''.join([' '*(pisos - x)+('**'*x)+'\n' for x in range(pisos)]))

pisos = 5
elemento = '*'
espacios = None


for i in range(pisos):
    espacios = ' '*(pisos - i)
    print(espacios + elemento)
    elemento = elemento + '**'
