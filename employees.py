# This file contains the Employee class, which is used to interact with the employee table in the database.
from database import c, conn


class Employee(object):
    def __init__(self, name, surname, age, gender, pk=None):
        self.id = pk
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    @classmethod
    def get(cls, pk):
        result = c.execute("SELECT * FROM employee WHERE id = ?", (pk,))
        row = result.fetchone()
        if row is None:
            return None
        employee = Employee(row["name"], row["surname"], row["age"], row["gender"], row["id"])
        return employee

    @classmethod
    def get_list(cls, **kwargs):
        conditions = []
        values = []
        for key, value in kwargs.items():
            if key == "name_like":
                conditions.append(f"name LIKE ?")
            elif key == "age_gt":
                conditions.append(f"age > ?")
            elif key in ["age", "gender"]:
                conditions.append(f"{key} = ?")
            else:
                conditions.append(f"{key} = ?")
            values.append(value)
        condition_str = " AND ".join(conditions)
        query = "SELECT * FROM employee"
        if condition_str:
            query += " WHERE " + condition_str
        result = c.execute(query, tuple(values))
        employees = []
        for row in result.fetchall():
            gender = row.get("gender") if "gender" in row else None
            employees.append(Employee(row["name"], row["surname"], row["age"], gender, row["id"]))
        return employees

    def __repr__(self):
        return f"<Employee {self.name} {self.surname}>"

    def update(self):
        c.execute("UPDATE employee SET name = ?, surname = ?, age = ?, gender = ? WHERE id = ?",
                  (self.name, self.surname, self.age, self.gender, self.id))

    def create(self):
        # check if an employee with the same name, surname, age, and gender already exists
        result = c.execute("SELECT id FROM employee WHERE name = ? AND surname = ? AND age = ? AND gender = ?",
                           (self.name, self.surname, self.age, self.gender))
        existing_employee = result.fetchone()
        if existing_employee:
            print("This employee already exists in the database.\n")
            return  # do not create a new record if employee already exists

        # insert the new employee record into the database
        c.execute("INSERT INTO employee (name, surname, age, gender) VALUES (?, ?, ?, ?)",
                  (self.name, self.surname, self.age, self.gender))
        self.id = c.lastrowid
        conn.commit()

    def save(self):
        if self.id is not None:
            self.update()
        else:
            self.create()
        conn.commit()
        return self

    def delete(self):
        c.execute("DELETE FROM employee WHERE id = ?", (self.id,))
        conn.commit()

    def __lt__(self, other):
        return self.age < other.age
