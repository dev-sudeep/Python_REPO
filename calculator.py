op=(input("Enter the operation you want to perform: \n- Addition\n- Subtraction\n- Multiplication\n- Division\n"))
n1=int(input("Enter the first number: \n"))
n2=int(input("Enter the second number: \n"))
if op=="Addition":
    sum=n1+n2
    print("The sum of the two numbers is: ",sum)
elif op=="Subtraction":
    diff=n1-n2
    print("The difference of the two numbers is: ",diff)
elif op=="Multiplication":
    prod=n1*n2
    print("The product of the two numbers is: ",prod)
elif op=="Division":
    div=n1/n2
    print("The division of the two numbers is: ",div)
else:
    print("Invalid operation")