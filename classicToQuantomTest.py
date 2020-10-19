import unittest, classicToQuantom as cq ,calculadoraVectoresMatrices as lib, math as m

class TestClassicToQuantum(unittest.TestCase):
    def testdeberiacalcprobabilidad(self):
        self.assertEqual(cq.observableProbabilidadMatriz((
            [(2,1),
            (-1,2),
            (0,1),
            (1,0),
            (3,-1),
            (2,0),
            (0,-2),
            (-2,1),
            (1,-3),
            (0,-1)]),7),10.87)

        self.assertEqual(cq.observableProbabilidadMatriz((
            [(2,1),
            (-1,2),
            (0,1),
            (1,0),
            (3,-1),
            (2,0),
            (0,-2),
            (-2,1),
            (1,-3),
            (0,-1)]),2),2.17) 


                               
    def testdeberiacalcamplitudtransicion(self):
        self.assertEqual(cq.amplitudDeTransicion([(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)],
                               [(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]),(-0.021,-0.13))

    def testdeberiacalcmedia(self):
        self.assertEqual(cq.media([[(1,0),(0,-1)],
                [(0,1),(2,0)]],
                [[(m.sqrt(2)/2,0)],
                [(0,m.sqrt(2)/2)]]),2.5)

    def testdeberiacalcvarianza(self):
        self.assertEqual(cq.varianza([[(1,0),(0,-1)],
                [(0,1),(2,0)]],
                [[(m.sqrt(2)/2,0)],
                [(0,m.sqrt(2)/2)]]),0.25)
    
    

    def testEjercicio4x3x2(self):
        initialState =  [(0,0),(0,-1)]
        estado1 = [(0,1),(1,0)]
        estado2 = [(0,-1),(1,0)]

        print("Probabilidad de transicion a 1 :: "+ str(cq.probabilidadDeTransicion(initialState,estado1)))
        print("Probabilidad de transicion a 2 :: "+ str(cq.probabilidadDeTransicion(initialState,estado2)))



        
    def testEjercicio_4_4_2(self):
        print("")
        print("----Ejercicio 4.4.2----")

        matrizAdyacencia = [[(0,0),(1/m.sqrt(2),0),(1/m.sqrt(2),0),(0,0)],
                            [(0,1/m.sqrt(2)),(0,0),(0,0),(1/m.sqrt(2),0)],
                            [(1/m.sqrt(2),0),(0,0),(0,0),(0,1/m.sqrt(2))],
                            [(0,0),(1/m.sqrt(2),0),(-1/m.sqrt(2),0),(0,0)],]

        estadoInicial = [[(1,0)],
                        [(0,0)],
                        [(0,0)],
                        [(0,0)]]

        estadofinal = cq.dinamica(matrizAdyacencia,estadoInicial,3)
        estadofinal = lib.transpuestaMatriz(estadofinal)
        probabilidad = cq.observableProbabilidadMatriz(estadofinal,3)


        print("Estado del sistema despues de 3 clicks: "+str(estadofinal))
        print("La probabilidad de encontrar la bola en la posición 3 es: "+ str(probabilidad))


if __name__ == '__main__' :
    unittest.main()