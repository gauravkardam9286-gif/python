my_str = "Python"
x=0
n= int(input("enter a number : "))
for i in range(n):
    for i in my_str:
        x+=1
        print(my_str[0:x])
    
    for i in my_str:
        x-=1
        print(my_str[0:x])
 
