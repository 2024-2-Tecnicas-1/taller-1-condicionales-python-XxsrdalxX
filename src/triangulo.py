def evaluar(a, b, c):
    # Verifica si el triángulo es válido
    if a + b > c and a + c > b and b + c > a:
        # Verifica si es equilátero
        if a == b == c:
            return "El triángulo es equilátero"
        # Verifica si es isósceles
        elif a == b or a == c or b == c:
            return "El triángulo es isósceles"
        # Si no es equilátero ni isósceles, es escaleno
        else:
            return "El triángulo es escaleno"
    else:
        return "No es un triángulo válido"

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)