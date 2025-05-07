def contar_vocales(palabra): #Defne la función
    
    # Solicita al usuario una palabra y cuenta cuántas vocales contie
    
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

# Interaccion usuario con la consola
palabra = input("Ingrese una palabra: ")

# Cuenta las vocales en la palabra
numero_vocales = contar_vocales(palabra)

# Imprime el resultado
print(f"La palabra '{palabra}' tiene {numero_vocales} vocales.")