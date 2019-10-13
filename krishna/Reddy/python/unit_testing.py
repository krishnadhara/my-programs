import unittest
class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupclass method executed... ")

    def setUp(self):
        print("setup methos executed...")

    def Test_method1(self):
        print("test_method1 method executed...")

    def Test_method2(self):
        print("test_method2 method executed...")
    def tearDown(self):
        print("teardown method executed...")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass method executed... ")
    unittest.main()

