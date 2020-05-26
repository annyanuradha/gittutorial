terms = int(input("enter the number of terms :"))
num1 = 0
num2 = 1
count = 0 


if terms<=0:
    print("invalid number")
elif terms==1:
    print("fibonacci sequence is:",num1,num2)
else:
    while count<=terms:
        print(num1)
        nth = num1+num2
        num1 = num2
        num2 = nth
        count+=1
