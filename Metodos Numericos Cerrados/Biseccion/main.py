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

#Aplicacion del metodo Numerico con Ciclo for
def metodoNumerico(a, b): #pasamos valores iniciales
    xa = a
    for i in range(1, maxIter):
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
            print(f"Iteracion numero {i}")
            break

    print(f"Error: {error}")
    print(f"La raiz aproximada en la iteracion es Xm con valor de: {round(Xm, cifrasDecimales)}")

#Aplicacion del metodo Numerico con ciclo While, permitiendo mantener la condicion de parada como el criterio para frenar independientemente del numero de iteracion como en el for
def metodoNumericoWhile(a, b): #pasamos valores iniciales
    #Bandera que indicara la iteracion
    i = 0
    xa = a
    error = 1e10
    while(error > epsilon):
        #Aumento en la bandera
        i += 1

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
            print(f"Iteracion numero {i}")
            break

    print(f"Error: {error}")
    print(f"La raiz aproximada en la {i} iteracion es Xm con valor de: {round(Xm, cifrasDecimales)}")

# metodoNumericoWhile(0, 2)
    
