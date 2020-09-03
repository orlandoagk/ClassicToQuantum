import unittest
from calculadoraVectoresMatrices import *

class testCalculadora(unittest.TestCase):
    def testSumaVectores(self):
        self.assertEqual(sumaVectores([(3,4),(8,9)],[(19,7),(-4,0)]),[(22, 11), (4, 9)])
        self.assertEqual(sumaVectores([(3,4),(8,9),(-14,0)],[(19,7),(-4,0),(32,-74)]),[(22, 11), (4, 9), (18, -74)])
        self.assertEqual(sumaVectores([(3,4),(8,-6)],[(946,7),(-4,0)]),[(949, 11), (4, -6)])

    def testVectorInverso(self):
        self.assertEqual(vectorInversoAditivo([(3,4),(8,0),(-9,0)]),[(-3, -4), (-8, 0), (9, 0)])
        self.assertEqual(vectorInversoAditivo([(6,5),(48,30),(-94,3)]),[(-6,-5),(-48,-30),(94,-3)])
        self.assertEqual(vectorInversoAditivo([(38,43),(-81,0),(-9,7)]),[(-38,-43),(81,0),(9,-7)])
    
    def testEscalarPorVector(self):
        self.assertEqual(escalarPorVector([(3,4),(8,0),(-9,0)],4),[(12, 16), (32, 0), (-36, 0)])
        self.assertEqual(escalarPorVector([(3,-37),(8,0),(-9,102)],94),[(282, -3478), (752, 0), (-846, 9588)])
        self.assertEqual(escalarPorVector([(8,24),(768,0),(34,12)],-8),[(-64, -192), (-6144, 0), (-272, -96)])
    
    def testAdicionMatrices(self):
        self.assertEqual(adicionMatrices([[(6,-3),(93,0)],[(-4,-47),(2,0)],[(53,674),(-84,32)]],[[(9,-2),(52,32)],[(-68,-3),(-5,7)],[(74,-246),(-34,65)]]),[[(15, -5), (145, 32)], [(-72, -50), (-3, 7)], [(127, 428), (-118, 97)]])
    
    def testMatrizInversoAditivo(self):
        self.assertEqual(matrizInversoAditivo([[(6,-3),(93,0)],[(-4,-47),(2,0)],[(53,674),(-84,32)]]),[[(-6, 3), (-93, 0)], [(4, 47), (-2, 0)], [(-53, -674), (84, -32)]])
    
    def testEscalarPorMatriz(self):
        self.assertEqual(escalarPorMatriz([[(6,-3),(93,0)],[(-4,-47),(2,0)],[(53,674),(-84,32)]],-4),[[(-24, 12), (-372, 0)], [(16, 188), (-8, 0)], [(-212, -2696), (336, -128)]])
    
    def testTranpuestaVector(self):
        self.assertEqual(transpuestaVector([(3, 4), (4, 6), (7, 8)]),[[(3, 4)], [(4, 6)], [(7, 8)]])
        self.assertEqual(transpuestaVector([[(3, 4)], [(4, 6)], [(7, 8)]]),[(3, 4), (4, 6), (7, 8)])
    
    def testTranspuestaMatriz(self):
        self.assertEqual(transpuestaMatriz([[(3,4),(9,8)],[(9,74),(-43,2)]]),[[(3,4),(9,74)],[(9,8),(-43,2)]])
    
    def testConjugadoMatriz(self):
        self.assertEqual(conjugadoMatriz([[(3,4),(9,8)],[(9,74),(-43,2)]]),[[(3, -4), (9, -8)], [(9, -74), (-43, -2)]])
    
    def testConjugadoVector(self):
        self.assertEqual(conjugadoVector([(3,49),(8,0),(74,-3)]),[(3,-49),(8,0),(74,3)])

    def testDagaVector(self):
        self.assertEqual(dagaVector([[(3,49)],[(8,0)],[(74,-3)]]),[(3, -49), (8, 0), (74, 3)])

    def testDagaMatriz(self):
        self.assertEqual(dagaMatriz([[(1,3),(2,3)],[(4,2),(5,1)]]),[[(1, -3), (4, -2)], [(2, -3), (5, -1)]])
    
    def testProductoMatrices(self):
        self.assertEqual(productoMatrices([[(1,3),(2,3)],[(4,2),(5,1)]],[[(1,2),(2,3),(4,1)],[(1,4),(3,2),(1,1)]]),[[(-15, 16), (-7, 22), (0, 18)], [(1, 31), (15, 29), (18, 18)]])
    
    def testProductoMatrizVector(self):
        self.assertEqual(productoMatrizPorVector([[(1,3),(2,3)],[(4,2),(5,1)]],[(1,2),(2,3)]),[[(-10, 17)], [(7, 27)]])
    
    def testNormaVector(self):
        self.assertEqual(normaVector([(3.1,7.1),(6.6,-6)]),11.814)
        self.assertEqual(normaVector([(3,4),(5,6),(9,0),(-19,74)]),77.485)
    
    def testDistanciaDosVectores(self):
        self.assertEqual(distanciaDosVectores([(3,5),(7,4)],[(9,1),(0,74)]),8.062)

if __name__ == '__main__' :
    unittest.main()