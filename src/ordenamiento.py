def evaluar(numero1, numero2, numero3, numero4):
    # Crea una lista con los cuatro números
    numeros = [numero1, numero2, numero3, numero4]
    
    # Ordena la lista de menor a mayor
    numeros.sort()
    
    # Devuelve la lista de números ordenados
    return numeros

if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)