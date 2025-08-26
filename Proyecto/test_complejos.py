import unittest
import math
import libreria_complejos as c

class TestLibreriaComplejos(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(c.suma((1, 2), (3, 4)), (4, 6))
        self.assertEqual(c.suma((0, 0), (0, 0)), (0, 0))
        self.assertEqual(c.suma((-1, -2), (1, 2)), (0, 0))

    def test_producto(self):
        self.assertEqual(c.producto((1,2), (3,4)), (-5,10))
        self.assertEqual(c.producto((0,0), (1,1)), (0,0))
        self.assertEqual(c.producto((1,0), (0,1)), (0,1))


    def  test_resta(self):
        self.assertEqual(c.resta((5,7), (2,3)), (3,4))
        self.assertEqual(c.resta((2,0), (0,1)), (2,-1))
        self.assertEqual(c.resta((2,0), (-2,0)), (4,0))

    def test_division(self):
        self.assertEqual(c.division((1,2), (3,4)), (0.44, 0.08))
        self.assertEqual(c.division((0,0), (1,1)), (0,0))
        with self.assertRaises(ValueError):
            c.division((1,1), (0,0))

    def test_modulo(self):
        self.assertAlmostEqual(c.modulo((3,4)), 5.0)
        self.assertAlmostEqual(c.modulo((0,0)), 0.0)
        self.assertAlmostEqual(c.modulo((-3,-4)), 5.0)

    def test_conjugado(self):
        self.assertEqual(c.conjugado((3,4)), (3,-4))
        self.assertEqual(c.conjugado((0,0)), (0,0))
        self.assertEqual(c.conjugado((-3,-4)), (-3,4))

    def test_polar_a_cartesiano(self):  
        test1 = c.polar_a_cartesiano(5, math.atan2(4,3))
        self.assertAlmostEqual(test1[0], 3)  # parte real
        self.assertAlmostEqual(test1[1], 4)  # parte imaginaria
        self.assertAlmostEqual(c.polar_a_cartesiano(0, 0), (0,0))
        test2 = c.polar_a_cartesiano(1, math.pi/2)
        self.assertAlmostEqual(test2[0], 0)  # parte real
        self.assertAlmostEqual(test2[1], 1)  # parte imaginaria
    
    def test_cartesiano_a_polar(self):
        self.assertAlmostEqual(c.cartesiano_a_polar((3,4)), (5, math.atan2(4,3)))
        self.assertAlmostEqual(c.cartesiano_a_polar((0,0)), (0,0))
        self.assertAlmostEqual(c.cartesiano_a_polar((0,1)), (1, math.pi/2))
    
    def test_fase(self):
        self.assertAlmostEqual(c.fase((1,1)), math.pi/4)
        self.assertAlmostEqual(c.fase((0,0)), 0)
        self.assertAlmostEqual(c.fase((0,1)), math.pi/2)
        self.assertAlmostEqual(c.fase((1,0)), 0)