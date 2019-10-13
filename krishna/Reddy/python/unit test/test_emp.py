import unittest
from employ import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Employee('krishna', 'reddy', 50000)
        self.emp_2 = Employee('dhara', 'reddy', 60000)
        print("setup")
    def tearDown(self):
        print("teardown")

    def trst_email(self):
        print("email")
        self.assertEqual(self.emp_1.email,'krishna.reddy@gmail.com')
        self.assertEqual(self.emp_2.email,'dhara.reddy@gmail.com')
        self.emp_1.first='sushmi'
        self.emp_2.first='nani'
        self.assertEqual(self.emp_1.email,'sushmi.reddy@gmail.com')
        self.assertEqual(self.emp_2.email, 'nani.reddy@gmail.com')

    def trst_fullname(self):
        print("fullname")
        self.assertEqual(self.emp_1.fullname,'krishna reddy')
        self.assertEqual(self.emp_2.fullname,'dhara reddy')
        self.emp_1.first='sushmi'
        self.emp_2.first='nani'
        self.assertEqual(self.emp_1.fullname,'sushmi reddy')
        self.assertEqual(self.emp_2.fullname, 'nani reddy')

    def test_apply_raise(self):
        print("raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay,52500)
        self.assertEqual(self.emp_2.pay,63000)
    @classmethod
    def setUpClass(cls):
        print("setup class")

    @classmethod
    def tearDownClass(cls):
        print("teardown class")
if __name__ =="__main__":
    unittest.main()
