# Autor: Santiago Camargo 

def main():
    nombre = ['santiago','pedro','sebastian']
    apellido = ['camargo','molina','amaya']
    edad = [23,17,32]
    print('Nombres: ',nombre)
    print('Apellidos: ',apellido)
    print('Edades: ',edad)
    dicc = {}
    for x in range(3):
        dicc.update(dict([
            ('Nombre',nombre[x]),
            ('Apellido',apellido[x]),
            ('Edad',edad[x])
        ]))
        print(dicc)

if __name__ == '__main__':
    main()