from main import *
#file = 'test.csv'
file = '../train_2.csv'
x, y = get_data(file)
reg(x,y)
print results
for i in range(1,1000):
    reg(x,y)
    print results
    print 'current :', i