x1=3
x2=21
xx=x1+x2
f = open('gnuplot.dat','w')
for c in range(1,100):
    f.write("%s " %c)
    x=c*c
    f.write("%s \n" %x)
f.close()
print("the end %i" %xx)
#print file('test').read()
#print file('a.py').read()
print("Ok!...")