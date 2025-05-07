def edades(x):
    if (x >= 0):
        if (x < 13):
            print ("El usuario se clasifica como Niño")
        elif (x >= 13 and x <= 17):
            print ("El usuario se clasifica como Adolescente")
        elif (x >= 18 and x <= 59):
            print ("El usuario se clasifica como Adulto")
        else:
            print ("El usuario se clasifica como Adulto mayor")
    else:
        print ("Error")

x = int(input("\033[35m===== BIENVENIDO AL CLASIFICADOR DE EDADES ====\033\n[0mIntroduce la edad: "))
edades(x)
