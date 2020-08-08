import unittest
import operacioncomplejos

class TestComplejos(unittest.TestCase):
    def testSuma(self):
        self.assertEqual(operacioncomplejos.suma((4,3),(1,-7)),(5,-4))
        self.assertEqual(operacioncomplejos.suma((0,1),(1,0)),(1,1))
        self.assertEqual(operacioncomplejos.suma((-10,1),(32,4)),(22,5))

    def testResta(self):
        self.assertEqual(operacioncomplejos.restar((4,3),(1,-7)),(3,10))
        self.assertEqual(operacioncomplejos.restar((-3,8),(-4,2)),(1,6))
        self.assertEqual(operacioncomplejos.restar((56,38),(6,-2)),(50,40))
    
    def testMultiplicacion(self):
        self.assertEqual(operacioncomplejos.producto((0,3),(0,2)),(-6,0))
        self.assertEqual(operacioncomplejos.producto((0,3),(0,-1)),(3,0))
        self.assertEqual(operacioncomplejos.producto((6,8),(4,2)),(8,44))

    def testDivision(self):
        self.assertEqual(operacioncomplejos.division((56,-8),(14,10)),(88/37,-84/37))
        self.assertEqual(operacioncomplejos.division((10,6),(5,-3)),(16/17,30/17))
        self.assertEqual(operacioncomplejos.division((5,2),(-2,3)),(-4/13,-19/13))

if __name__ == "__main__":
    unittest.main()