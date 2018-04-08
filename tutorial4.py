
class Employee:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@company.de'
		self.pay = pay

	def fullname():
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
	pass


dev_1 = Developer('kraus', 'klein', 64)
dev_2 = Developer('inger', 'klein', 82)

print(dev_1.email)
print(dev_2.email)