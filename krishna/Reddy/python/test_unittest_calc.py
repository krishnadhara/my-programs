import unittest
import calc
import kvr
class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setup_class method ")
    @classmethod
    def tearDownClass(cls):
        print("teardown class method")
    def setUp(self):
        print("set_method execute**********")
    def tearDown(self):
        print("tear down method")
    def test_add(self):
        result=calc.add(10,5)
        self.assertEqual(result,15)
        print("add method  +++++")
    def test_sub(self):
        result=calc.sub(10,5)
        self.assertEqual(result,5)
        print("sub method --------")
    def test_mul(self):
        result=calc.mul(10,5)
        self.assertEqual(result,50)
        print("mul method @@@@@@@")
if "__init__"=='__main__':
    unittest.main()

class unittestdemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("SET_CLASS")
    @classmethod
    def tearDownClass(cls):
        print("TEAR_DOWN")

    def setUp(self):
        print(" SET_up")
    def tearDown(self):
        print("TEAR")
    def test_first(self):
        a=kvr.joinstring("krishna","dhara")
        a=kvr.uppercase(a)
        self.assertEqual(a,"KRISHNADHARA")
        print("first")
    def test_second(self):
        a=kvr.lowercase("KRISHNADHARA")
        self.assertEqual(a,"krishnadhara")
        print("second")
    def test_thrad(self):
        a=kvr.uppercase("krishnadhara")
        self.assertEqual(a,"KRISHNADHARA")
        print("threed")
if "__init__"=='__main__':
    unittest.main()




