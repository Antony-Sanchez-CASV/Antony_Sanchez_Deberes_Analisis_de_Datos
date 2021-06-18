#Desarrollar una aplicación que me permita multiplicar matrices con numpy.
#El usuario debe ingresar las dimensiones de las matrices
#y los datos de la misma.
#Se debe validar las dimensiones y los datos ingresados.

import numpy as np
def introducirM(f,c):
    print("Matriz de: (",f," x ",c,")")
    print("Por favor ingrese los valores de la matriz")
    pila=[]
    total=f*c
    for i in range(total):
        print("Ingrese el valor de la fila ",(((i)%f)+1)," columna ",(int((i/f))+1))
        pila.append(int(input()))
    matriz=np.reshape(pila,(f,c))
    print("La Matriz ingresada es: \n",matriz)
    return matriz
    
print("Bienvenidos")
print("En este programa podra multiplicar matrices")

print("Primera matriz")
print("Por favor introduce el numero de filas")
f1=int(input())

print("Por favor introduce el numero de columnas")
c1=int(input())
matriz1=introducirM(f1,c1)
print()
print("Segunda matriz")
print("Para poder multiplicar las filas deben ser iguales a las columnas \nde la primera matriz")
print("Las filas son: ",c1)
print()
print("Recuerde que las columnas de la segunda matriz deben ser igual o menor \na las filas de la primera matriz")

f2=c1

while True:
    print("Por favor introduce el numero de columnas. Maximo: ",f1)
    c2=int(input())
    if c2<=f1:
        break
    else:
        print("Valor erroneo. ",end="")
matriz2=introducirM(f2,c2)

matrizR=np.dot(matriz1,matriz2)
print()
print("Las matrices a multiplicar son: ")
print("Matriz 1 de: (",f1," x ",c1,")\n",matriz1,"\nMatriz 2de: (",f2," x ",c2,")\n",matriz2)

print("La matriz resulatante:\n",matrizR,"\nCreado por:\nAntony Sanchez\nJohan Quinatoa\nBryan Quisaguano\nJhosef Rea\n\n\n\n")
        
