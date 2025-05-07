def edades(x): #Definición de función
    if (x >= 0): #Primera condición ser mayor o tener de 0 años
        if (x < 13): #Segunda condición
            print ("El usuario se clasifica como Niño")
        elif (x >= 13 and x <= 17): #Tercera condición un intervalo de edades
            print ("El usuario se clasifica como Adolescente")
        elif (x >= 18 and x <= 59): #Cuarta condición segundo intervalo de edades
            print ("El usuario se clasifica como Adulto")
        else: #Todo lo que no cumpla las anteriores condiciones
            print ("El usuario se clasifica como Adulto mayor")
    else: # Si el usuario typea una edad menor a 0
        print ("Error")

x = int(input("\033[35m===== BIENVENIDO AL CLASIFICADOR DE EDADES ====\033\n[0mIntroduce la edad: "))
edades(x) # Menu e interacción con el usuario
