# Employee Management System
This Python script provides functionalities to interact with an employee database using the Employee class defined 
in the employees.py module. Below is a guide to understanding and utilizing this system effectively.
# Setup
Ensure you have the following prerequisites:
- Python installed on your system.
- Access to an SQL database where the employee table is stored.
- Necessary permissions to read, write, update, and delete records in the employee table.
- Structure
- `employees.py`: Contains the Employee class definition.
- `main.py`: Executes various test cases to demonstrate the usage of Employee class methods.
- `database.py`: Contains database connection settings and helper functions for database operations.
- `README.md`: This file, providing an overview and guide for the Employee Management System.
- `requirements.txt`: Contains the required Python packages for this project.

# Usage
1) Initialization: Ensure you have configured the database connection settings in database.py correctly.

2) Testing Methods:
Modify the test cases in main.py as per your requirements. The provided test cases demonstrate:
    - Retrieving employees based on various criteria such as age, gender, and name.
    - Creating a new employee record.
    - Updating an existing employee record.
    - Deleting an employee record.
    - Comparing employees based on their age.

3) Running the Application:
    - Execute main.py to run the test cases and observe the output in the console. Ensure that the database connection is active and properly configured before executing the script.

# 'Employee' Class Methods
- get_list(): Retrieves a list of employees based on specified criteria such as age, gender, or name pattern.
- get(): Retrieves a single employee record by their unique identifier (id).
- create(): Creates a new employee record in the database.
- update(): Updates an existing employee record in the database.
- delete(): Deletes an employee record from the database.
- Comparison: Employees can be compared based on their age using standard comparison operators.

# Modifying the Code
- Extend the functionalities of the Employee class by adding new methods as required.
- Modify database queries or add new ones to suit your specific needs.
- Ensure proper error handling to deal with potential issues during database operations.

# Additional Notes
- The provided test cases in main.py are for demonstration purposes. Modify them as per your requirements.
- Ensure that the database connection settings in database.py are accurate and up-to-date.

> Gvantsa