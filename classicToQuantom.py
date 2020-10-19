from calculadoraVectoresMatrices import *

def dinamica(M,v,t):

    """ Description permite hacer cambios en el estado del sistema
    
    :type M: matriz
    :param M: Matriz usada en la libreria cuantica
    :type v: lista
    :param v: Vector usado en la libreria cuantica
    :type t: entero
    :param t: Número de iteracciones
    :rtype: matriz
    """
    matrizAuxiliar = M
    for x in range(t):
        matrizAuxiliar = productoMatrices(matrizAuxiliar,M)
    valorARetonar = productoMatrizPorVector(matrizAuxiliar,v)
    return valorARetonar

def observableProbabilidadMatriz(m,x):
    
    """ Description calcula la probabilidad de encontrar una particula en una posición x 
    :type m: matriz
    :param m: matriz que describe el estado
    :type x: entero
    :param x: posición de la de que se desea encontrar la probabilidad
    :rtype: flotante con dos decimas de redondeo
    """

    operacion = (modulo(m[x])**2/normaVector(m)**2)*100
    return round(operacion,2)

def media(omega, ket):
    
    """ Description calcula la media de omega en un estado
    :type omega: matriz
    :param omega: matriz
    :type ket: vector horizontal
    :param ket: estado
    :rtype: flotante con dos decimas de redondeo
    """

    productoOmegaKet = transpuestaMatriz(productoMatrices(omega,ket))
    ketTranspuesto = transpuestaMatriz(ket)
    valorARetonar = productoInterno(productoOmegaKet,ketTranspuesto)
    return round(valorARetonar[0],2)


def delta(omega,ket):

    """ Description calcula el delta de omega en un estado
    :type omega: matriz
    :param omega: matriz
    :type ket: vector horizontal
    :param ket: estado
    :rtype: matriz
    """

    mediaValue = media(omega,ket)
    identidad = matrizIdentidad(omega)
    res = escalarPorMatriz(mediaValue,identidad)
    restaOmega = restaMatrices(omega,res)
    return restaOmega

def varianza(omega,ket): 

    """ Description calcula la varianza de un omega con un estado
    :type omega: matriz
    :param omega: matriz
    :type ket: matriz 
    :param ket: estado
    :rtype: flotante con dos decimas de redondeo
    """
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

def probabilidadDeTransicion(ket1,ket2):
    ampt = amplitudDeTransicion(ket1,ket2)
    mod = modulo(ampt)
    return mod