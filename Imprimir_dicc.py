# Autor: Santiago Camargo 

def main():
    dicc = {
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

    for i in dicc:
        print(f"Clave:{i} - Valor:{dicc[i]}")

if __name__ == '__main__':
    main()