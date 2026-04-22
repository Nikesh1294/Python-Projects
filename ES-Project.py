class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: ₹{self.salary}"


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, salary):
        emp = Employee(name, age, salary)
        self.employees.append(emp)
        print(f"Employee '{name}' added successfully.")

    def list_employees(self):
        if not self.employees:
            print("No employees found.")
            return

        print("\n--- Employee List ---")
        for emp in self.employees:
            print(emp)

    def delete_by_age_range(self, min_age, max_age):
        before_count = len(self.employees)
        self.employees = [
            emp for emp in self.employees
            if not (min_age <= emp.age <= max_age)
        ]
        deleted = before_count - len(self.employees)
        print(f"{deleted} employee(s) deleted.")

    def find_employee(self, name):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                return emp
        return None

    def update_salary(self, name, new_salary):
        emp = self.find_employee(name)
        if emp:
            emp.salary = new_salary
            print(f"Salary updated for {name}.")
        else:
            print(f"Employee '{name}' not found.")


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def run_demo(self):
        print("=== Employee System Running (Auto Demo Mode) ===\n")

        # Adding employees
        self.manager.add_employee("Swaraj", 22, 30000)
        self.manager.add_employee("Rahul", 28, 45000)
        self.manager.add_employee("Priya", 24, 40000)

        # Listing employees
        self.manager.list_employees()

        # Update salary
        print("\nUpdating salary of Rahul...")
        self.manager.update_salary("Rahul", 50000)

        # Find employee
        print("\nSearching for Priya...")
        emp = self.manager.find_employee("Priya")
        if emp:
            print("Found:", emp)

        # Delete by age range
        print("\nDeleting employees between age 23 and 30...")
        self.manager.delete_by_age_range(23, 30)

        # Final list
        self.manager.list_employees()



if __name__ == "__main__":
    app = FrontendManager()
    app.run_demo()