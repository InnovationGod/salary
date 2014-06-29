'''
Created on 7 Mar 2013

@author: eidahil
'''

class SalaryData(object):
    
    def __init__(self, gross_salary, take_home_pay, first_gross_salary, first_take_home_pay, year_current, year_one):
        self.set_my_gross_salary(gross_salary)
        self.set_my_monthly_take_home_pay(take_home_pay)
        self.set_my_first_gross_salary(first_gross_salary)
        self.set_my_first_monthly_take_home_pay(first_take_home_pay)
        self.set_year_current(year_current)
        self.set_year_one(year_one)

    ''' my gross salary '''
    def set_my_gross_salary(self, my_gross_salary):
        self.gross_salary = my_gross_salary

    def get_my_gross_salary(self):
        return self.gross_salary

    ''' my take home pay '''
    def set_my_monthly_take_home_pay(self, my_take_home_pay):
        self.take_home_pay = my_take_home_pay

    def get_my_monthly_take_home_pay(self):
        return self.take_home_pay
    
    ''' my first year salary '''
    def set_my_first_gross_salary(self, my_gross_salary):
        self.first_gross_salary = my_gross_salary

    def get_my_first_gross_salary(self):
        return self.first_gross_salary

    ''' my first year salary take home pay '''
    def set_my_first_monthly_take_home_pay(self, my_take_home_pay):
        self.first_take_home_pay = my_take_home_pay

    def get_my_first_monthly_take_home_pay(self):
        return self.first_take_home_pay
    
    ''' Current Year '''
    def set_year_one(self, my_year_one):
        self.year_one = my_year_one

    def get_year_one(self):
        return self.year_one
    
    ''' First Year '''
    def set_year_current(self, my_year_current):
        self.year_current = my_year_current

    def get_year_current(self):
        return self.year_current
    
    ''' find number of years '''
    def get_number_of_years_in_service(self):
        num_years =  (self.get_year_current() - self.get_year_one())
        return num_years
   
   
    
