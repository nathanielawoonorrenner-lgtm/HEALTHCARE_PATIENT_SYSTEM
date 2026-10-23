class Employee:
    company_name = 'yayo & sons Limited'
    total_employees = 0
    def __init__(self, name, employee_id,
                 deparment, salary,
                            hire_date,
                            position,
                            email,
                            hourly_rate,
                            university):
        self.name = name
        self.employee_id = employee_id
        self.deparment = deparment
        self.salary = salary
        self.hire_date = hire_date
        self.is_active = True
        self.position = position
        self.email = email
        self.hourly_rate = hourly_rate
        self.university = university
        Employee.total_employees += 1

    def get_employee_info(self):
        return f'''
        Name = {self.name}
        Employee_id = {self.employee_id}
        Deparment = {self.deparment}
        salary = {self.salary}
        Hire_date = {self.hire_date}
        position = {self.position}
        email = {self.email}
        university = {self.university}
        Active = {self.is_active}
        '''

    def calculate_annual_salary(self):
    weekly_salary = self.hourly_rate * 40
    annual_salary = weekly_salary * 52
    return annual_salary

   def get_year_of_service(self):
       current_year = 2026
       years = current_year - self.hire_date
       return years
   def terminate_employee(self):
       self.is_active = False
   def update_email(self, new_email):

   @classmethod
   def get_company_name(cls):
       return cls.company_name
   @classmethod
   def get_total_employees(cls):
       return cls.total_employees

