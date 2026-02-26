import numpy as np # type: ignore

#Condicion de parada
epsilon = 1e-10
maxIter = 100

#Numero de cifras decimales
cifrasDecimales = 5


def funcionDeX(x):
    return ((np.exp(x)) + x - 2)

def funcionXm(a, b):
    return (a+b)/2

#Aplicacion del metodo Numerico
def metodoNumerico(a, b): #pasamos valores iniciales
    xa = a
    for i in range(1, 100+1):
        print(f"Iteracion numero {i}")
        #calculo de xm
        Xm = funcionXm(a, b)
        error = abs(xa - Xm)
        xa = Xm

        if(funcionDeX(a) * funcionDeX(Xm) < 0): #hay cambio de signo, por tanto, la raiz esta entre esos
            # print("El cambio de signo esta entre f(a) y f(Xm)")
            b = Xm

        elif(funcionDeX(b) * funcionDeX(Xm) < 0): #hay cambio de signo, por tanto, la raiz esta entre esos
            a = Xm
            # print("El cambio de signo esta entre f(b) y f(Xm)")
        
        # else:
        #     print(f"La raiz es Xm con valor de: {Xm}")
        #     break

        if(error < epsilon):
            break

    print(f"Error: {error}")
    print(f"La raiz aproximada en la iteracion es Xm con valor de: {round(Xm, cifrasDecimales)}")

metodoNumerico(0, 2)
    
