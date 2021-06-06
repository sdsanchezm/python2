from math import pi

year = 2018
price = 3.547974
print('- average in year %d is $ %f' % (year, price))
print('- average in year %i is $ %3.2f' % (year, price))
print('- average in year %i is $ %08.2f' % (year, price))
print('- average in year %d is $ %e' % (year, price))
print('- average in year %d is $ %3.2e' % (year, price))
print('- average in year %d is $ %3.2E' % (year, price))
print("Right adjusted: %20.8f" %(pi))

data = [["Suresh Datta", 57394, "suresh@example.com"], ["Colette Browning", 48539, "colette@example.com"], ["Skye Homsi", 58302, "skye@example.com"], ["Hiroto Yamaguchi", 48502, "hiroto@example.com"], ["Tobias Ledford", 48291, "tobias@example.com", "Tamara Babic", 58201, "tamara@example.com"], ["Jin Xu", 48293, "jin@example.com"], ["Joana Dias", 23945, "joana@example.com"], ["Alton Derosa", 85823, "alton@example.com"]]

print("Name " % (data))

print('Right adjusted : {:_<20.2f}'.format(pi))
print('Center adjusted: {:_^20.2f}'.format(pi))
print('Left adjusted  : {:_>20.2f}'.format(pi))

#print(' | {0:14} | {1:14} | {2:<14} | ')
print('| {:_<21} | {:<21} | {:<21} |'.format(" "," "," "))
print(' | {:_>20.2f} | '.format(year))
print(' | {:_^20.2f} | '.format(year))
print("| {:_^21} | {:_^21} | {:_^21} |".format("_","_", "_"))
print("| {:^21} | {:^21} | {:^21} |".format("Name","ID", "Email"))
print("| {:-^21} | {:-^21} | {:-^21} |".format("-","-", "-"))

for i in data:
		#print("| {:_^21} | {:_^21} | {:_^21} |" .format(i[0],i[1],i[2]), end=" ")
		print("| {:^21} | {:^21} | {:^21} |" .format(i[0],i[1],i[2]), end=" ")
		#print(j, end=" ")
		print(end="\n")

print(end="\n")
print(end="\n")

print(data)
print(data[1][0],data[1][1],data[1][2])