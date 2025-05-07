def Numeros(A , B , C, D , E): # Definición de función

                if (A % 2 != 0 or A <= 0): #Condiciones para cada numero
                        A = 0
                if (B % 2 != 0 or B <= 0):
                        B = 0
                if (C % 2 != 0 or C <= 0):
                        C = 0
                if (D % 2 != 0 or D <= 0):
                        D = 0
                if (E % 2 != 0 or E <= 0 ):
                        E = 0
                
                return A + B + C + D + E #Suma de los numeros siguiendo esas condiciones
                
        
        

A = int(input("\033[35m===== BIENVENIDO AL ANALIZADOR ==== \n\033[0mEscribe un numero: ")) #Interacción del usuario con consola (poner numeros)
B = int(input("Escribe otro numero: "))
C = int(input("Escribe otro numero: "))
D = int(input("Escribe otro numero: "))
E = int(input("Escribe otro numero: "))


print (f"\033[32m==== RESULTADOS ====\033\n[0mLa suma de los numeros pares positivos es {Numeros(A , B , C , D , E)}") #Impresión de los resultados

