import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError, EmployeeError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        # TODO add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        # TODO you'll need to modify PhoneAssignments.add_phone() to make this test pass
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)



    def test_create_and_add_new_employee(self):
        # TODO write this test and then remove the self.fail() statement
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        ee1 = Employee(1, 'Mary')
        ee2 = Employee(2, 'Bill')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(ee1)
        testAssignmentMgr.add_employee(ee2)

        self.assertIn(ee1, testAssignmentMgr.employees)
        self.assertIn(ee2, testAssignmentMgr.employees)


    def test_create_and_add_employee_with_duplicate_id(self):
        # TODO write this test and then remove the self.fail() statement
        # TODO you'll need to fix the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id

        testPhone1 = Phone(1, 'Apple', 'iPhone 1')
        testPhone2 = Phone(2, 'Apple', 'iPhone 2')

        ee1 = Employee(1, 'Mary')
        ee2 = Employee(1, 'Bill')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.assign(1, ee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(1, ee2)


    def test_assign_phone_to_employee(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments

        testAssignmentMgr = PhoneAssignments()
        testPhone1 = Phone(1, 'Apple', 'iPhone 1')
        testPhone2 = Phone(2, 'Apple', 'iPhone 2')

        ee1 = Employee(1, 'Mary')
        ee2 = Employee(2, 'Bill')

        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.assign(1, ee1)
        testAssignmentMgr.assign(2, ee2)

        #for ee in testAssignmentMgr.employees:
        #    print(ee)
        #for phone in testAssignmentMgr.phones:
        #    print(phone)


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee.
        # A PhoneError should be raised.
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone
        # is alreaady assigned.

        testAssignmentMgr = PhoneAssignments()
        testPhone1 = Phone(1, 'Apple', 'iPhone 1')
        testPhone2 = Phone(2, 'Apple', 'iPhone 2')

        ee1 = Employee(1, 'Mary')
        ee2 = Employee(2, 'Bill')

        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        #for ee in testAssignmentMgr.employees:
        #    print(ee)
        #for phone in testAssignmentMgr.phones:
        #    print(phone)

        testAssignmentMgr.assign(1, ee1)
        testAssignmentMgr.assign(2, ee2)


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError
        # if the phone is alreaady assigned.

        testAssignmentMgr = PhoneAssignments()
        testPhone1 = Phone(1, 'Apple', 'iPhone 1')
        testPhone2 = Phone(2, 'Apple', 'iPhone 2')

        ee1 = Employee(1, 'Mary')
        ee2 = Employee(2, 'Bill')

        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.assign(1, ee1)
        testAssignmentMgr.assign(2, ee2)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(1, ee1)


#        self.fail()


    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.

#        self.fail()

        testAssignmentMgr = PhoneAssignments()
        testPhone1 = Phone(1, 'Apple', 'iPhone 1')
        testPhone2 = Phone(2, 'Apple', 'iPhone 2')

        ee1 = Employee(1, 'Mary')
        ee2 = Employee(2, 'Bill')

        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.assign(1, ee1)
        testAssignmentMgr.assign(2, ee2)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(1, ee1)


    def test_un_assign_phone(self):
        # TODO write this test and remove the self.fail() statement
        # Assign a phone, unasign the phone, verify the employee_id is None

        testAssignmentMgr = PhoneAssignments()
        testPhone1 = Phone(1, 'Apple', 'iPhone 1')
        testPhone2 = Phone(2, 'Apple', 'iPhone 2')

        ee1 = Employee(1, 'Mary')
        ee2 = Employee(2, 'Bill')

        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.assign(1, ee1)
        testAssignmentMgr.assign(2, ee2)

        testAssignmentMgr.un_assign(1)

        for ph in testAssignmentMgr.phones:
            if ph.id == 1:
                self.assertFalse(ph.is_assigned())


    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        testAssignmentMgr = PhoneAssignments()
        testPhone1 = Phone(1, 'Apple', 'iPhone 1')
        testPhone2 = Phone(2, 'Apple', 'iPhone 2')

        ee1 = Employee(1, 'Mary')
        ee2 = Employee(2, 'Bill')
        #ee3 = Employee(3, 'Nobody')
        ee3 = Employee(None, None)

        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)
        testAssignmentMgr.add_employee(ee1)
        testAssignmentMgr.add_employee(ee2)

        testAssignmentMgr.assign(1, ee1)


        # error   FAILED (errors=1)
        #num = 0
        #print(5 / num)

        # FAILED   FAILED (failures=1)
        #with self.assertRaises(EmployeeError):
        #    testAssignmentMgr.phone_info(ee2)




        self.assertTrue(testAssignmentMgr.phone_info(ee1))
        self.assertFalse(testAssignmentMgr.phone_info(ee1))

        # TODO check that the method returns None if the employee does not have a phone
        self.assertEqual(None, testAssignmentMgr.phone_info(ee2))

        # TODO check that the method raises an PhoneError if the employee does not exist
        with self.assertRaises(EmployeeError):
            testAssignmentMgr.phone_info(ee3)



if __name__ == '__main__':
    TestPhoneManager()
