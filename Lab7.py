from typing import override

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        return f"Имя: {self.name}, ID: {self.emp_id}"


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    @override
    def get_info(self):
        return super().get_info() + f", Отдел: {self.department}"

    def manage_project(self, project_name):
        return f"Менеджер {self.name} управляет проектом: {project_name}"


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    @override
    def get_info(self):
        return super().get_info() + f", Специализация: {self.specialization}"

    def perform_maintenance(self, equipment):
        return f"Техник {self.name} выполняет обслуживание: {equipment}"


class TechManager(Employee):
    def __init__(self, name, emp_id, department, specialization):
        super().__init__(name, emp_id)
        self.department = department
        self.specialization = specialization
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)
        return f"Сотрудник {employee.name} добавлен в команду {self.name}."

    def get_team_info(self):
        if not self.team:
            return f"У {self.name} нет членов команды."
        return "\n".join([member.get_info() for member in self.team])

    @override
    def get_info(self):
        return super().get_info() + f", Отдел: {self.department}, Специализация: {self.specialization}"

    def manage_project(self, project_name):
        return f"Менеджер {self.name} управляет проектом: {project_name}"

    def perform_maintenance(self, equipment):
        return f"Техник {self.name} выполняет обслуживание: {equipment}"


employee = Employee("Алиса", 101)
manager = Manager("Боб", 102, "Кадры")
technician = Technician("Чарли", 103, "Сетевое оборудование")
tech_manager = TechManager("Диана", 104, "ИТ", "Системное администрирование")

print(employee.get_info())
print(manager.get_info())
print(manager.manage_project("Кадровый проект"))
print(technician.get_info())
print(technician.perform_maintenance("Роутер"))

print(tech_manager.get_info())
print(tech_manager.manage_project("Модернизация инфраструктуры"))
print(tech_manager.perform_maintenance("Сервер"))
print(tech_manager.add_employee(employee))
print(tech_manager.add_employee(technician))
print(tech_manager.get_team_info())