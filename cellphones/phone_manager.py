# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)


class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)


#    #add method to check for equality between objects - Jeremy
#    def __eq__(self, other):
#        return self.id == other.id and self.name == other.name



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):
        # TODO raise exception if two employees with same ID are added
        # spin through employee list and check for matching employees
        for emp in self.employees:
            if emp.id == employee.id:
                raise EmployeeError('Employee %s already exists, can\'t add again' % employee)

        self.employees.append(employee)  # original code


    def add_phone(self, phone):
        # TODO raise exception if two phones with same ID are added
        for p in self.phones:
            if p.id == phone.id:
                raise PhoneError('Phone %s already exists, can\'t add again' % phone)

        self.phones.append(phone)


    def assign(self, phone_id, employee):
        # Find phone in phones list
        # TODO if phone is already assigned to an employee, do not change list, raise exception
        # TODO if employee already has a phone, do not change list, and raise exception
        # TODO if employee already has this phone, don't make any changes. This should NOT raise an exception.

        for phone in self.phones:
            # make initial phone assignment

            if phone.id == phone_id and phone.employee_id == None:
                phone.assign(employee.id)
                return

            # TODO if phone is already assigned to an employee, do not change list, raise exception
            elif phone.id == phone_id and phone.employee_id != None:
                raise PhoneError('Some Employee %s already has this phone, can\'t make assignment' % employee)

            # TODO if employee already has a phone, do not change list, and raise exception
            elif employee.id == phone.employee_id:
                raise PhoneError('This Employee %s already has a phone, can\'t make assignment' % employee)

            # TODO if employee already has this phone, don't make any changes. This should NOT raise an exception.
            elif phone.id == phone_id and phone.employee_id and phone.is_assigned() == None:
                return


    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):
        # find phone for employee in phones list

        # TODO  should return None if the employee does not have a phone
        # TODO  the method should raise an exception if the employee does not exist

        employeeFound = False

        for ee in self.employees:
            if ee.id == employee.id:
                employeeFound = True
                break
            else:
                employeeFound = False

        if not employeeFound:
            raise EmployeeError('Employee %s not found' % employee)

        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone

        return None


# delete/comment out the following code - Jeremy
#class PhoneError(Exception):
#    pass

# add class to handle Employee raised exceptions
class EmployeeError(Exception):
    """ Custom exception class """
    pass

# add class to handle Phone raised exceptions
class PhoneError(Exception):
    """ Custom exception class """
    pass

