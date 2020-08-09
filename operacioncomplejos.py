import math

def suma(x1,x2):
    primerValor = int(x1[0])+int(x2[0])
    segundoValor = int(x1[1])+int(x2[1])
    valorRetornar = (primerValor,segundoValor)
    return valorRetornar

def restar(x1,x2):
    primerValor = int(x1[0])-int(x2[0])
    segundoValor = int(x1[1])-int(x2[1])
    valorRetornar = (primerValor,segundoValor)
    return valorRetornar

def producto(x1,x2):
    resta = x1[0]*x2[0]-x1[1]*x2[1]
    suma = x1[0]*x2[1]+x1[1]*x2[0]
    valorRetornar = (resta,suma)
    return valorRetornar

def division(x1,x2):
    primeraParteArriba = x1[0]*x2[0]+x1[1]*x2[1]
    primeraParteAbajo = (x2[0]**2)+(x2[1]**2)
    if(primeraParteAbajo==0):
        raise NameError("División por 0")
    segundaParteArriba = x1[1]*x2[0]-x1[0]*x2[1]
    valorRetornar = (primeraParteArriba/primeraParteAbajo,segundaParteArriba/primeraParteAbajo)
    return valorRetornar

def modulo(x1):
    valorRetornar = ((x1[0]**2)+(x1[1]**2))**0.5

    return valorRetornar

def conjugado(x1):
    parteImaginaria = 0
    if(x1[1]!= 0):
        parteImaginaria = x1[1]*-1
    valorRetornar = (x1[0],parteImaginaria)
    return valorRetornar

def argumento(x1):
    if(x1[0] == 0):
        raise NameError("La parte real no puede ser 0")
    return math.atan2(x1[1],x1[0])

def polar(x1):
    return (modulo(x1),argumento(x1))

def cartesiano(x1):
    parteReal = round(x1[0]*math.cos(x1[1]))
    parteImaginaria = round(x1[0]*math.sin(x1[1]))
    return (parteReal,parteImaginaria)


#print(cartesiano((5.385164807134504,0.3805063771123649)))
#print(division((5,-3),(2,1)))