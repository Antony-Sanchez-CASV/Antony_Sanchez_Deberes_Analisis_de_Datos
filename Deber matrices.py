#Realizar una multiplicación de matrices,
#la cual tiene valores que son ingresados por el usuario.
#El usuario también debe definir la dimensión de las matrices.
#Subir en el aula virtual el código y captura de pantallas de la ejecución.

def introducirM(f,c):#crea una matriz con datos introducidos por el usuario
    matriz=[]
    
    for i in range(f):
        matrizAuxiliar=[]#crea una matriz pequeña por fila
        for j in range(c):
            print("Introduce numero de fila: ",i+1," columna: ",j+1)
            matrizAuxiliar.append(int(input()))
        matriz.append(matrizAuxiliar)#añade la fila a la matriz
    return matriz
def multiplicacion(m1,m2):  
    matrizResultado=[]
    for i in range(len(m1)):
        datos=[]
        for k in range(len(m1)):
            dato=0
            for j in range(len(m1[i])):#sumatoria
                dato+=m1[i][j]*m2[j][k]#dato correspondiente de la multiplicacion de matrices
            datos.append(dato)#añade un dato a una fila
        matrizResultado.append(datos)#añade una fila a la matriz
    return matrizResultado
            
print("Bienvenidos")
print("En este programa podra multiplicar matrices")
print("Tomar en cuenta que se creara matrices compatibles automaticamente")
print("Primera matriz")
print("Por favor introduce el numero de filas")
f=int(input())

print(("Por favor introduce el numero de columnas"))
c=int(input())
print("La matriz 1 es de: ",f," x ",c)
print("La matriz 2 es de: ",c," x ",f,end="\n\n")
print("Introduce la primera matriz")
m1=introducirM(f,c)
print("Matriz 1: ",m1)
print("")

print("Introduce la segunda matriz")
m2=introducirM(c,f)
print("Matriz 2: ",m1)
print("")
mResultado=multiplicacion(m1,m2)
print("La matriz resultante: \n", mResultado)
