# This file contains the Employee class, which is used to interact with the employee table in the database.
# You can change test cases in main.py to test the Employee class methods.
from employees import Employee


def main():
    # test get_list() method
    print("List of employees with age 21:")
    employees_with_age_21 = Employee.get_list(age=21)
    for employee in employees_with_age_21:
        print(f"{employee.name} {employee.surname}")

    print()
    print("List of female employees with age 23:")
    young_female_employees = Employee.get_list(gender="female", age=23)
    for employee in young_female_employees:
        print(f"{employee.name} {employee.surname}")
    print()

    print("List of employees whose name starts with 'G' and age is above 20:")
    employees_with_name_g = Employee.get_list(name_like="G%", age_gt=20)
    for employee in employees_with_name_g:
        print(f"{employee.name} {employee.surname}, Age: {employee.age}")
    print()

    # test get() method
    employee = Employee.get(1)
    if employee:
        print(f"Employee with id 1:", {employee.name, employee.surname}, "\n")

    # test create() method
    new_employee = Employee("Charles", "Leclerc", 26, "male")
    new_employee.create()

    # test update() method
    employee_to_update = Employee.get(7)
    if employee_to_update:
        print(f"Updating employee:", {employee_to_update.name, employee_to_update.surname})
        employee_to_update.name = "Daisy"
        employee_to_update.update()
        print(f"Employee updated:", {employee_to_update.name, employee_to_update.surname}, "\n")

    # test delete() method
    employee_to_delete = Employee.get(10)
    if employee_to_delete:
        print(f"Deleting employee:", {employee_to_delete.name, employee_to_delete.surname}, "\n")
        employee_to_delete.delete()

    # test comparison based on age
    employee1 = Employee.get(2)
    employee2 = Employee.get(3)
    if employee1 and employee2:
        if employee1 < employee2:
            print(f"{employee1.name, employee1.surname} is younger than {employee2.name, employee2.surname}")
        else:
            print(f"{employee2.name, employee2.surname} is younger than {employee1.name, employee1.surname}")


if __name__ == "__main__":
    main()
