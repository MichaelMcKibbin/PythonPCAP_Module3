class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.__employee_id = employee_id
        self.__base_salary = base_salary

    def display_info(self):
        print(f"Name: {self.name}, Employee ID: {self.__employee_id}, Salary: {self.__base_salary}")

    def get_name(self):
        return self.name

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def set_base_salary(self, base_salary):
        self.__base_salary = base_salary

    def get_base_salary(self):
        return self.__base_salary

    def get_total_pay(self):
        #return self.__base_salary
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, bonus, benefits):
        super().__init__(name, employee_id, base_salary)
        self.__bonus = bonus
        self.__benefits = benefits

    def display_info(self):
        super().display_info()
        print(f"Benefits: {self.__benefits}")

    def get_name(self):
        return self.name

    def get_base_salary(self):
        return self.__base_salary

    def get_benefits(self):
        return self.__benefits

    def get_total_pay(self):
        return self.__base_salary + self.__bonus + self.__benefits


class ContractEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, overtime_pay, overtime_hours, contract_duration):
        super().__init__(name, employee_id, base_salary)
        self.__overtime_pay = overtime_pay
        self.__overtime_hours = overtime_hours
        self.__contract_duration = contract_duration

    def display_info(self):
        super().display_info()
        print(f"Contract Duration: {self.__contract_duration}")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_contract_duration(self):
        return self.__contract_duration

    def set_contract_duration(self, contract_duration):
        self.__contract_duration = contract_duration

    def get_overtime_pay(self):
        return self.__overtime_pay

    def set_overtime_pay(self, overtime_pay):
        self.__overtime_pay = overtime_pay

    def get_overtime_hours(self):
        return self.__overtime_hours

    def set_overtime_hours(self, overtime_hours):
        self.__overtime_hours = overtime_hours

    def get_base_salary(self):
        return self.__base_salary

    def set_base_salary(self, base_salary):
        self.__base_salary = base_salary


    def get_total_pay(self):
        return self.__base_salary + (self.__overtime_pay * self.__overtime_hours)