import unittest
import calk

class TestCalk(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calk.add(10,5),15)
        self.assertEqual(calk.add(-5, 5),0)
        self.assertEqual(calk.add(-10, -5), -15)
        self.assertEqual(calk.add(10, 5), 15)
    def test_sub(self):
        self.assertEqual(calk.sub(10,5),5)
        self.assertEqual(calk.sub(5, -5),10)
        self.assertEqual(calk.sub(-10, -5), -5)
        self.assertEqual(calk.sub(-10, 5), -15)
    def test_mul(self):
        self.assertEqual(calk.mul(10,5),50)
        self.assertEqual(calk.mul(-5, 5),-25)
        self.assertEqual(calk.mul(-10, -5), 50)
        self.assertEqual(calk.mul(1, 5), 5)
    def test_div(self):
        self.assertEqual(calk.div(10,5),2)
        self.assertEqual(calk.div(-5, 5),-1)
        self.assertEqual(calk.div(-10, -5), 2)

        #self.assertRaises(ValueError,calk.div,10,0)
        #with self.assertRaises(ValueError):

if __name__ =='main':
    unittest.main()