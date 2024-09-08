def evaluar(caracter):
 # Verificar si es un número
    if caracter.isdigit():
        return "Es número"
    # Verificar si es una letra
    elif caracter.isalpha():
        if caracter.isupper():
            return "Es letra mayúscula"
        else:
            return "Es letra minúscula"
    # Si no es letra ni número
    else:
        return "No es letra ni número"


if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
