
class Employee:
	pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Ser'
emp_1.last = 'Sank'
emp_1.email = 'ser.sank@etwas.de'
emp_1.pay = 42000

emp_2.first = 'Leoc'
emp_2.last = 'cord'
emp_2.email = 'leoc.cord@etwas.de'
emp_2.pay = 21000

print(emp_1.email)
print(emp_2.email)