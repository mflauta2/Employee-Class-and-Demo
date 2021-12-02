Github: https://github.com/mflauta2/Employee-Class-and-Demo
Employee Class: 
            Employee class contains the properties and method for an employee. So whenever users 
            create an object of employee class he/she can access the public properties of the employee. 
            For now all variables are private in this employee class. So the only way to access them using 
            the getter and setter methods. In this class we have id, name, age, salary of the employee. 
            Along with that we have some methods totalSalary, calculateBonus and viewDetails for the employee.

id variable: 
    This variable defines the id of the employee. It should be an int type variable.
    This variable is a private variable so that the only way to access this variable is 
    using getter and setter methods

name variable: 
             This variable defines the names of the employee. It should be a string type variable.
             This variable is private and the only way to access this variable using getter and setter 
             that is defined in employee class.

age variable: 
            This variable defines the age of the employee. It should be a int type variable.
            This variable is private and the only way to access this variable using getter and setter 
             that is defined in employee class.

salary variable: 
            This variable defines the salary of the employee. It is a float type variable.
            This variable is private and the only way to access this variable using getter and setter 
             that is defined in employee class.

bonus variable:
                This variable define the bonus of the salary of employee. It is a float type variable.

get_total_salary method:
                        This method take no parameter. This method returns us the total salary of employee.
                        This total salary of employee is calculated by sum of salary and bonus of the employee.


calculateBonus method:
                        This method take no parameter. This method returns the bonus earned by employee.
                        12% bonus are calculated of the employee's salary and store it into the bonus variable.
                        This method returns the bonus of the employee.
    
viewDetails method:
                    This method does not take any parameter and does not return any value. This function displays
                    the employee details such as id, name, age, salary, bonus and total salary.
                    



Documentation
                Whenever users run this program it asks for input from the user.
                The user will enter id, name, age, salary in the input and press enter. After that 
                the details for the user will be displayed. 
    

How to Run ?

To run this program just write command
1. python main.py

After program will wait for user input
2. Enter employee id: 1
   Enter employee name: john
   Enter employee age: 30
   Enter Employee salary: 1000

After that the employee information will be shown in output
3. Id: 1
   Name: john
   Age: 30
   Salary: 1000.0
   Bonus: 120.0
   Total Salary: 1120.0