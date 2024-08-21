# Autor: Santiago Camargo 

def conca_dicc(dicc1, dicc2):
    list2 = dicc2.keys()
    for i in dicc1.keys():
        if i in list2:
            dicc2.pop(i)
    dicc1.update(dicc2)
    return dicc1

def main():
    dicc1 = {
        'num1': 23,
        'num2': 14,
        'num3': 45,
        'num4': 67,
        'num5': 1
    }

    dicc2 = {
        'num4': 89,
        'num6': 9,
        'num7': 100,
        'num8': 56,
        'num9': 32
    }
    print(f"diccionario 1: {dicc1}")
    print(f"diccionario 2: {dicc2}")
    print(f"El nuevo diccionario es: {conca_dicc(dicc1,dicc2)}")

if __name__ == '__main__':
    main()