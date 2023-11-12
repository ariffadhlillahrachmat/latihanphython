class Employee:
    def _init_(self, name):
        self.name = name
        self.base_salary = 4000000
        self.daily_allowance = 30000
        self.absent = False

    def calculate_salary(self):
        if not self.absent:
            return self.base_salary + self.daily_allowance
        else:
            return self.base_salary

    def display_info(self):
        print(f"Employee: {self.name}")
        print(f"Base Salary: {self.base_salary}")
        print(f"Daily Allowance: {self.daily_allowance}")
        print(f"Absent: {'No' if not self.absent else 'Yes'}")
        print(f"Total Salary: {self.calculate_salary()}")
        print("\n")


class Manager(Employee):
    def _init_(self, name):
        super()._init_(name)
        self.professional_allowance = 1500000
        self.daily_transport_allowance = 30000

    def calculate_salary(self):
        if not self.absent:
            return (
                self.base_salary
                + self.daily_allowance
                + self.professional_allowance
                + self.daily_transport_allowance
            )
        else:
            return self.base_salary + self.professional_allowance

    def display_info(self):
        print("Manager Information:")
        super().display_info()
        print(f"Professional Allowance: {self.professional_allowance}")
        print(f"Daily Transport Allowance: {self.daily_transport_allowance}")


class Admin(Employee):
    def _init_(self, name, overtime_hours=0):
        super()._init_(name)
        self.overtime_rate = 40000
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        if not self.absent:
            return (
                self.base_salary
                + self.daily_allowance
                + (self.overtime_rate * self.overtime_hours)
            )
        else:
            return self.base_salary

    def display_info(self):
        print("Admin Information:")
        super().display_info()
        print(f"Overtime Rate: {self.overtime_rate}")
        print(f"Overtime Hours: {self.overtime_hours}")


class Marketing(Employee):
    def _init_(self, name):
        super()._init_(name)
        self.daily_transport_allowance = 50000

    def calculate_salary(self):
        return self.base_salary + self.daily_transport_allowance

    def display_info(self):
        print("Marketing Information:")
        super().display_info()
        print(f"Daily Transport Allowance: {self.daily_transport_allowance}")


# Main method
if _name_ == "_main_":
    manager1 = Manager("John Doe")
    admin1 = Admin("Jane Doe", overtime_hours=2)
    marketing1 = Marketing("Alice Wonderland")

    # Simulate absence for Admin
    admin1.absent = True

    # Display information
    manager1.display_info()
    admin1.display_info()
    marketing1.display_info()