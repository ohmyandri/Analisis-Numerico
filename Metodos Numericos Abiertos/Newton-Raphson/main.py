import numpy as np # type: ignore

#Condiciones de parada
epsilon = 1e-3

#Definimos la funcion para valuar en la funcion
def f(x):
    return ((np.exp(-x)) - x + 2)

#Definimos la funcion para valuar en la f prima
def fp(x):
    return ( -(np.exp(-x)) - 1 )

def metodoNumericoNewtonRaphson(a): #a es el valor inicial
    #Condiciones Iniciales y valor a buscar
    x0 = 0 #En esta variable guardaremos el valor anterior digamos es la x (i - 1)
    xi = a

    #Error actual, iniciado en 1e10 para poder iniciar el ciclo
    error = 1e10

    #Mientras nuestro error, sea mayor o igual a la tolerancia que pusimos, es decir continuara sucediendo asta que el error sea menor a la condicion de parada
    while(error >= epsilon):
        # xi = x0 #Marcamos a xi como el punto en que estamos
        xi = xi - (f(xi))/(fp(xi))

        #Calculamos el error
        error = abs(xi - x0)

        #Guardamos el xi que teniamos
        x0 = xi

        #Calculamos el nuevo xi

        print(xi)

metodoNumerico(1)