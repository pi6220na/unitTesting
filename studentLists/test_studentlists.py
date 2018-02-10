'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    ## TODO write a test that adds and removes a student, and asserts the student is removed. Use assertNotIn
    def test_add_remove_assert(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)



    ## TODO write a test that removes a student not in the list, and asserts a StudentError is raised
    def test_remove_assert_error(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student 1')
        test_class.add_student('Test Student 2')
        #self.assertNotIn('Test Student 3', test_class.class_list)
        with self.assertRaises(StudentError):
            test_class.remove_student('Test Student 3')


    ## TODO write a test that removes a student from an empty list, and asserts a StudentError is raised
    def test_empty_list_assert_error(self):
        test_class = ClassList(0)
        self.assertNotIn('Test Student 3', test_class.class_list)
        with self.assertRaises(StudentError):
            test_class.remove_student('Test Student 3')



    def test_enrollment_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_enrollment_empty_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))



    ## TODO write a test that adds some example students to a test class, call check_enrolled
    # for a student not enrolled, assert check_enrolled returns false
    def test_check_enrolled_function(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student 1')
        test_class.add_student('Test Student 2')
        self.assertFalse(test_class.is_enrolled('Test Student 3'))


    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', test_class.__str__())


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', test_class.__str__())


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))
        #self.assertIsNone(test_class.index_of_student('Harry')) #this fails with "AssertionError: 1 is not None"

    ## However, it would be useful to check that index_of_student returns None if a student isn't present.
    ## TODO write a test for index_of_student to assert it returns None if the student is not in the list
    # Cover the cases where the list is empty
    # And, when the list is not empty but does not contain the student name.
    def test_for_None_in_list(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')
    #List not empty
        self.assertEqual(None, test_class.index_of_student('Betty'))
    #List is empty
        test_class.remove_student('Harry')
        test_class.remove_student('Hermione')
        test_class.remove_student('Ron')
        self.assertEqual(None, test_class.index_of_student('Betty'))



    ## TODO write a test(s) for your new is_class_full method
    ## Test a case where the class is full, and when it isn't
    def test_is_class_full(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')
    # test for full class condition
        self.assertTrue(test_class.is_class_full())
    # test for not a full class condition
        test_class.remove_student('Harry')
        self.assertFalse(test_class.is_class_full())


