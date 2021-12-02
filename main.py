# Matthew Flauta
# Assignment 10.1: Your Own Class

# Defining a Employee class 
class Employee:

    '''
        * Create a employee with the specified details
        * @param id The employee's id 
        * @param name The employee's name 
        * @param age The employee's age 
        * @param salary The employee's salary 
    '''
    def __init__(self, id, name, age, salary):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__salary = salary
    
    '''
        * Gets the id of employee
        * @return id of employee
    '''
    def get_id(self):
        return self.__id
    
    '''
        * Sets the employee id
        * @param id an int containing employee id
    '''
    def set_id(self, id):
        self.__id = id
    

    '''
        * Gets the name of employee
        * @return name of employee
    '''
    def get_name(self):
        return self.__name
    
    
    '''
        * Sets the employee name
        * @param name a string containing employee name
    '''
    def set_name(self,name):
        self.__name = name
    

    '''
        * Gets the age of employee
        * @return age of employee
    '''
    def get_age(self):
        return self.__age
    

    '''
        * Sets the employee age
        * @param age an int containing employee age
    '''
    def set_age(self,age):
        self.__age = age


    '''
        * Gets the salary of employee
        * @return salary of employee
    '''
    def get_salary(self):
        return self.__salary
    

    '''
        * Sets the employee salary
        * @param salary a float containing employee salary
    '''
    def set_salary(self,salary):
        self.__salary = salary

    '''
        * Get the total calculated salary of employee
        * @return the total salary of employee
    '''
    def get_total_salary(self):
        return (self.__salary + self.__bonus)
    
    '''
        * Get the 12% bonus of employee
        * @return the bonus of employee 
    '''
    def calculateBonus(self):
        self.__bonus = 0.12 * self.__salary
        return self.__bonus

    '''
        * Show the details of employee
        * This function print the employee details: id, name, age, salary, bonus, total salary
    '''
    def viewDetails(self):
        print("Id: "+str(self.__id))
        print("Name: "+self.__name)
        print("Age: "+str(self.__age))
        print("Salary: "+str(self.__salary))
        print("Bonus: "+str(self.calculateBonus()))
        print("Total Salary: "+str(self.get_total_salary()))

def main():
    # here we are creating two objects of employee with name employee1 and employee2
    employee1 = Employee(1, "John Doe", 40, 18000)
    employee1.viewDetails()
    print("============================================")
    employee2 = Employee(2, "Adam Smith", 32, 10000)
    employee2.viewDetails()

if __name__ == "__main__":
    main()
   