# Autor: Santiago Camargo 

def main():
    dicc1 = {
        'num1': 23,
        'num2': 14,
        'num3': 45,
        'num4': 67,
        'num5': 1,
        'num6': 9,
        'num7': 100,
        'num8': 56,
        'num9': 32,
    }

    dicc2 = {
        'num1': 45,
        'num2': 14,
        'num3': 23,
        'num4': 67,
        'num5': 6,
        'num6': 98,
        'num7': 12,
        'num8': 55,
        'num9': 33,
    }

    dicc3 = {
        'num6': 9,
        'num7': 100,
        'num8': 56,
        'num9': 32,
        'num1': 23,
        'num2': 14,
        'num3': 45,
        'num4': 67,
        'num5': 1,
    }

    if dicc1 == dicc2:
        print("Los diccionarios 1 y 2 contienen las mismas clave:valor")
    elif dicc1 == dicc3:
        print("Los diccionarios 1 y 3 contienen las mismas clave:valor")
    else:
        print("Los diccionarios no comparten las mismas clave:valor")

if __name__ == '__main__':
    main()