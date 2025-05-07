def Numeros(A , B , C, D , E): # Definición de función

        if (A % 2 == 0):
                return A
        if (B % 2 == 0):
                return B
        
        if (C % 2 == 0):
                return C
        
        if (D % 2 == 0):
                return D
        if (E % 2 == 0):
                return E
        
        
        return A + B + C + D + E
        
        



A = int(input("\033[35m===== BIENVENIDO AL ANALIZADOR ==== \n\033[0mEscribe un numero: "))
B = int(input("Escribe otro numero: "))
C = int(input("Escribe otro numero: "))
D = int(input("Escribe otro numero: "))
E = int(input("Escribe otro numero: "))


print (f"\033[32m==== RESULTADOS ====\033\n[0mLa suma de los numeros pares positivos es {Numeros(A , B , C , D , E)}")

