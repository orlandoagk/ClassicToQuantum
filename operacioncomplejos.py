import math

def suma(x1,x2):
    
        """ Esta función realiza una suma entre dos numeros complejos
        :type x1: tupla de la forma (x,y)
        :param x1: x es la parte real e y la parte imaginaria
    
        :type x2: tupla de la forma (x,y)
        :param x2: x es la parte real e y la parte imaginaria
    
        :rtype: tupla (x,y)
        """
    primerValor = int(x1[0])+int(x2[0])
    segundoValor = int(x1[1])+int(x2[1])
    valorRetornar = (primerValor,segundoValor)
    return valorRetornar

def restar(x1,x2):
    
        """ Esta función realiza una resta entre dos numeros complejos
        :type x1: tupla de la forma (x,y)
        :param x1: x es la parte real e y la parte imaginaria
    
        :type x2: tupla de la forma (x,y)
        :param x2: x es la parte real e y la parte imaginaria
    
        :rtype: tupla (x,y)
        """
    primerValor = int(x1[0])-int(x2[0])
    segundoValor = int(x1[1])-int(x2[1])
    valorRetornar = (primerValor,segundoValor)
    return valorRetornar

def producto(x1,x2):
        """ Esta función halla el producto entre dos numeros complejos
        :type x1: tupla de la forma (x,y)
        :param x1: x es la parte real e y la parte imaginaria
    
        :type x2: tupla de la forma (x,y)
        :param x2: x es la parte real e y la parte imaginaria
    
        :rtype: tupla (x,y)
        """
    resta = x1[0]*x2[0]-x1[1]*x2[1]
    suma = x1[0]*x2[1]+x1[1]*x2[0]
    valorRetornar = (resta,suma)
    return valorRetornar

def division(x1,x2):
        """ Esta función realiza una division entre dos numeros complejos
        :type x1: tupla de la forma (x,y)
        :param x1: x es la parte real e y la parte imaginaria
    
        :type x2: tupla de la forma (x,y)
        :param x2: x es la parte real e y la parte imaginaria
        
        :raises: División por 0

        :rtype: tupla (x,y)
        """
    primeraParteArriba = x1[0]*x2[0]+x1[1]*x2[1]
    primeraParteAbajo = (x2[0]**2)+(x2[1]**2)
    if(primeraParteAbajo==0):
        raise NameError("División por 0")
    segundaParteArriba = x1[1]*x2[0]-x1[0]*x2[1]
    valorRetornar = (primeraParteArriba/primeraParteAbajo,segundaParteArriba/primeraParteAbajo)
    return valorRetornar

def modulo(x1):
    
        """ Esta funcion permite encontrar el modulo de un número complejo
        :type x1: tupla de la forma (x,y)
        :param x1: x es la parte real e y la parte imaginaria

        :rtype: un número flotante redondeado en 3 unidades
        """
    valorRetornar = ((x1[0]**2)+(x1[1]**2))**0.5

    return round(valorRetornar,3)

def conjugado(x1):
        """ Esta funcion permite encontrar el conjugado de un número complejo
        :type x1: tupla de la forma (x,y)
        :param x1: x es la parte real e y la parte imaginaria

        :rtype: una tupla de la forma (x,y)
        """
    parteImaginaria = 0
    if(x1[1]!= 0):
        parteImaginaria = x1[1]*-1
    valorRetornar = (x1[0],parteImaginaria)
    return valorRetornar

def argumento(x1):
        """ Esta funcion permite encontrar el argumento de un número complejo
        :type x1: tupla de la forma (x,y)
        :param x1: x es la parte real e y la parte imaginaria

        :raises: La parte real no puede ser 0

        :rtype: un número flotante redondeado en 3 unidades
        """
    if(x1[0] == 0):
        raise NameError("La parte real no puede ser 0")
    return round(math.atan2(x1[1],x1[0]),3)

def polar(x1):
        """ Esta funcion permite encontrar la forma polar de un número complejo
        :type x1: tupla de la forma (x,y)
        :param x1: x es la parte real e y la parte imaginaria

        :rtype: Una tupla donde el primer elemento es el modulo y el segundo es el argumento (angulo)
        """
    return (modulo(x1),argumento(x1))

def cartesiano(x1):
        """ Esta funcion permite encontrar la forma cartesiano de un número complejo
        :type x1: tupla de la forma (x,y)
        :param x1: x es la parte real e y la parte imaginaria

        :rtype: Una tupla donde el primer elemento es la parte real y la segunda es la parte imaginaria
        """
    parteReal = round(x1[0]*math.cos(x1[1]),3)
    parteImaginaria = round(x1[0]*math.sin(x1[1]),3)
    return (parteReal,parteImaginaria)


#print(cartesiano((5.385164807134504,0.3805063771123649)))
#print(division((5,-3),(2,1)))