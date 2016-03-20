from main import *
file_name = 'test.csv'
#file_name = '../train_2.csv'
x, y = get_data(file_name)
reg(x,y)
print results
for i in range(1,1000):
    reg(x,y)
    print results
    print 'current :', i