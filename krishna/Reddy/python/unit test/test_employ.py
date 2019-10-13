import unittest
from employ import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        print("setup")
    def tearDown(self):
        print("teardown")
    def trst_email(self):
        print("first")
        emp_1=Employee('krishna','reddy',1000)
        emp_2=Employee('dhara','reddy',2000)
        self.assertEqual(emp_1.email,'krishna.reddy@gmail.com')
        self.assertEqual(emp_2.email,'dhara.reddy@gmail.com')
        emp_1.first='sushmi'
        emp_2.first='nani'
        self.assertEqual(emp_1.email,'sushmi.reddy@gmail.com')
        self.assertEqual(emp_2.email, 'nani.reddy@gmail.com')
    def trst_fullname(self):
        print("second")
        emp_1=Employee('krishna','reddy',1000)
        emp_2=Employee('dhara','reddy',2000)
        self.assertEqual(emp_1.fullname,'krishna reddy')
        self.assertEqual(emp_2.fullname,'dhara reddy')
        emp_1.first='sushmi'
        emp_2.first='nani'
        self.assertEqual(emp_1.fullname,'sushmi reddy')
        self.assertEqual(emp_2.fullname, 'nani reddy')
    def test_apply_raise(self):
        print("three")
        emp_1=Employee('krishna','reddy',50000)
        emp_2=Employee('dhara','reddy',60000)
        emp_1.apply_raise()
        emp_2.apply_raise()
        self.assertEqual(emp_1.pay,52500)
        self.assertEqual(emp_2.pay,63000)
if __name__ =="__main__":
    unittest.main()
