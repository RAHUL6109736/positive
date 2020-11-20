mylist=[]
#list of 5 integer
for i in range(0,5):
    mylist.append(int(input('enter the int;')))
print(mylist)
print('positive number are= ')
for num in mylist:
    if num>=0:
        print(num,end=', ')
