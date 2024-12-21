class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return self.name, self.id


class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def manage_project(self):
        print(f"{self.name} управляет проектом")

    def get_info(self):
        return self.name, self.id, self.department


class Technician(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        print(f"{self.name} провел техобслуживание")

    def get_info(self):
        return self.name, self.id, self.specialization


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Employee.__init__(self, name, id)
        self.department = department
        self.specialization = specialization
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        return [s.get_info() for s in self.team]


emp1 = Employee("Oleg", 1)
emp2 = Employee("Alex", 2)
emp3 = Employee("Bob", 3)
admin = TechManager("Admin", 1, "Technician", "Security")

admin.add_employee(emp1)
admin.add_employee(emp2)
admin.add_employee(emp3)
admin.perform_maintenance()
admin.manage_project()

for employee in admin.team:
    print(employee.id, employee.name)
