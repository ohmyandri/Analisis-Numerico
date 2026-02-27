import numpy as np # type: ignore

#Condiciones de parada
epsilon = 0.0111
cifrasDecimales = 3

#Definimos la funcion para valuar en la funcion
def f(x):
    return ((np.exp(x)) + x - 2)

#Definimos la funcion para obtener xr
def xr(a, b):
    return (b - ((f(b)*(b - a))/(f(b)-f(a))))

def metodoNumericoReglaFalsa(a, b): #pasamos valores iniciales
    #Bandera que indicara la iteracion
    i = 0
    xa = a
    error = 1e10
    while(error > epsilon):
        #Aumento en la bandera
        i += 1

        #calculo de xm
        Xm = round(xr(a, b), cifrasDecimales)
        error = abs(xa - Xm)
        xa = Xm

        if(f(a) * f(Xm) < 0): #hay cambio de signo, por tanto, la raiz esta entre esos
            # print("El cambio de signo esta entre f(a) y f(Xm)")
            b = Xm

        elif(f(b) * f(Xm) < 0): #hay cambio de signo, por tanto, la raiz esta entre esos
            a = Xm
            # print("El cambio de signo esta entre f(b) y f(Xm)")
        
        # else:
        #     print(f"La raiz es Xm con valor de: {Xm}")
        #     break

        if(error < epsilon):
            print(f"El proceso se termino en la iteracion numero {i}")
            break

    print(f"Error: {error}")
    print(f"La raiz aproximada en la {i} iteracion es Xm con valor de: {round(Xm, cifrasDecimales)}")

metodoNumericoReglaFalsa(0, 2)