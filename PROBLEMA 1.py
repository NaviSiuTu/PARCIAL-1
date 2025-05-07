def Numeros(Z): # Definición de función
        if (A, B , C , D ,E % 2 == 0 and A, B, C, D, E>= 0): #Definición de condiciones
                
                result = A + B + C + D + E
                return result 

        if (A % 2 == 0):
                return A
                if (A % 2 == 0):
                return A



A = int(input("\033[35m===== BIENVENIDO AL ANALIZADOR ==== \n\033[0mEscribe un numero: "))
B = int(input("Escribe otro numero: "))
C = int(input("Escribe otro numero: "))
D = int(input("Escribe otro numero: "))
E = int(input("Escribe otro numero: "))
Z = A , B , C ,D, E

print (f"\033[32m==== RESULTADOS ====\033\n[0mLa suma de los numeros pares positivos es {Numeros(Z)}")

