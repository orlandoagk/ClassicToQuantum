from operacioncomplejos import *

def sumaVectores(vectorA,vectorB):
    if(len(vectorA)!=len(vectorB)):
        raise "Los vectores deben tener la misma dimensión"
    
    vectorSumado = []
    for i in range(len(vectorA)):
        vectorSumado.append(suma(vectorA[i],vectorB[i]))

    return vectorSumado

def vectorInversoAditivo(vectorA):
    return escalarPorVector(vectorA,-1)

def escalarPorVector(vectorA,escalar):
    devolverVector = []
    for i in range(len(vectorA)):
        tmp = (vectorA[i][0]*escalar,vectorA[i][1]*escalar)
        devolverVector.append(tmp)
    return devolverVector

def adicionMatrices(matrizA,matrizB):
    if(len(matrizA)!=len(matrizB) and len(matrizA[0])!=len(matrizB[0])):
        raise "Las matrices deben tener la misma dimensión"
    matrizDevolver = []
    for i in range(len(matrizA)):
        matrizDevolver.append(sumaVectores(matrizA[i],matrizB[i]))
    return matrizDevolver

def matrizInversoAditivo(matrizA):
    matrizDevolver = []
    for i in range(len(matrizA)):
        matrizDevolver.append(vectorInversoAditivo(matrizA[i]))
    return matrizDevolver

def escalarPorMatriz(matrizA,escalar):
    matrizDevolver = []
    for i in range(len(matrizA)):
        matrizDevolver.append(escalarPorVector(matrizA[i],escalar))
    return matrizDevolver

def transpuestaVector(vectorA):
    matrizDevolver = []
    for x in vectorA:
        if(type(x) is list):
            matrizDevolver.append(x[0])
        else:
            matrizDevolver.append([x])
    return matrizDevolver

def transpuestaMatriz(matrizA):
    matrizDevolver = []
    for i in range(len(matrizA)):
        for x in range(len(matrizA[i])):
            if(i==0):
                matrizDevolver.append([matrizA[i][x]])
            else:
                matrizDevolver[x].append(matrizA[i][x])
    return matrizDevolver

def conjugadoVector(vectorA):
    for i in range(len(vectorA)):
        vectorA[i] = conjugado(vectorA[i])
    return vectorA

def conjugadoMatriz(matrizA):
    for i in range(len(matrizA)):
        for i2 in range(len(matrizA[i])):
            matrizA[i][i2] = conjugado(matrizA[i][i2])
    return matrizA

def dagaVector(vectorA):
    return conjugadoVector(transpuestaVector(vectorA))

def dagaMatriz(matrizA):
    return conjugadoMatriz(transpuestaMatriz(matrizA))

def productoVectores(vectorA,vectorB):
    if(len(vectorA)!=len(vectorB)):
        raise "Estos vectores no se pueden multiplicar"
    vectorResultante = []
    for x in range(len(vectorA)):
        vectorResultante.append(producto(vectorA[x],vectorB[x]))
    return vectorResultante

def sumaVector(vector):
    valorDevolver = vector.pop(0)
    while len(vector)!=0:
        valorDevolver = suma(valorDevolver,vector.pop(0))
    return valorDevolver

def productoMatrices(matrizA,matrizB):
    if(len(matrizA[0])!=len(matrizB)):
        raise "Estas matrices no se pueden multiplicar"
    matrizResultante = []
    for x in range(len(matrizA)):
        tmp = []
        for y in range(len(matrizB[0])):
            tmp.append((x,y))
        matrizResultante.append(tmp)
    matrizBtranspuesta = transpuestaMatriz(matrizB)
    for i in range(len(matrizResultante)):
        for i2 in range(len(matrizResultante[i])):
            vectorTMP = productoVectores(matrizA[matrizResultante[i][i2][0]],matrizBtranspuesta[matrizResultante[i][i2][1]])
            matrizResultante[i][i2] = sumaVector(vectorTMP)
    return matrizResultante

def productoMatrizPorVector(matriz,vector):
    return productoMatrices(matriz,transpuestaVector(vector))

def productoInterno(vectorA,vectorB):
    if(len(vectorA)!=len(vectorB)):
        raise "Los vectores deben tener la misma longitud"
    dVA = dagaVector(vectorA)
    vectoresDaga = []

    for x in dVA:
        vectoresDaga.append(x[0])
    vectorTMP = productoVectores(vectoresDaga,vectorB)
    return sumaVector(vectorTMP)

def normaVector(vector):
    suma = 0
    for x in range(len(vector)):
        suma+= (vector[x][0])**2
        suma+= (vector[x][1])**2
    
    return round(math.sqrt(suma),3)

def restaVectores(vectorA,vectorB):
    if(len(vectorA)!=len(vectorB)):
        raise "No se puede restar estos vectores"
    matrizResultante = []
    for x in range(len(vectorA)):
        matrizResultante.append(restar(vectorA[x],vectorB[0]))
    return matrizResultante

def distanciaDosVectores(vectorA,vectorB):
    return normaVector(restaVectores(vectorA,vectorB))

def matrizIdentidad(M):

    identidad = [[(0,0) for i in range(len(M))] for j in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M)):
            if (i==j):
                identidad[i][j]=(1,0)
            else:
                identidad[i][j]=(0,0)
    return identidad

def restaMatrices(M,N):
    
    
    if (len(M) != len(N)):
        raise Exception("Las dimensiones de las matrices deben ser iguales")
    else:
        rta = []
        for i in range(len(M)):
            rta.append(restaVectores(M[i],N[i]))
    return rta