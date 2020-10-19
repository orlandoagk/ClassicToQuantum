from calculadoraVectoresMatrices import *

def observableProbabilidadMatriz(m,x):
    operacion = (modulo(m[x])**2/normaVector(m)**2)*100
    return round(operacion,2)


def media(omega, ket):
    productoOmegaKet = transpuestaMatriz(productoMatrices(omega,ket))
    ketTranspuesto = transpuestaMatriz(ket)
    valorARetonar = productoInterno(productoOmegaKet,ketTranspuesto)
    return round(valorARetonar[0],2)

def varianza(omega,ket): 
    deltaValor = delta(omega,ket)
    rta = productoMatrices(deltaValor,deltaValor)
    mediaValor = media(rta,ket)
    return mediaValor


def amplitudDeTransicion(kethA,kethB):
    normaKethA = normaVector(kethA)  
    normaKethB = normaVector(kethB)
    productoNormas = normaKethA * normaKethB
    div = division(productoInterno(kethA,kethB),(productoNormas,0))
    return div

def delta(omega,ket):
    mediaValue = media(omega,ket)
    identidad = matrizIdentidad(omega)
    res = escalarPorMatriz(mediaValue,identidad)
    restaOmega = restaMatrices(omega,res)
    return restaOmega

def dinamica(M,v,t):
    matrizAuxiliar = M
    for x in range(t):
        matrizAuxiliar = productoMatrices(matrizAuxiliar,M)
    valorARetonar = productoMatrizPorVector(matrizAuxiliar,v)
    return valorARetonar


def probabilidadDeTransicion(ket1,ket2):
    ampt = amplitudDeTransicion(ket1,ket2)
    mod = modulo(ampt)
    return mod