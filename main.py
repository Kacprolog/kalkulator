print("Selec an operation: ")
print("1.Addition")
print("2.Subtraction")
print("3.Divide")
print("4.Multiplication")

operator = input()

if operator == '1':
    num1 = input("Entry a number")
    num2 = input("Entry a number")
    print (str(int(num1) + int(num2)))
elif operator == '2':
    num1 = input("Entry a number")
    num2 = input("Entry a number")
    print (str(int(num1) - int(num2)))
elif operator == '3':
    num1 = input("Entry a number")
    num2 = input("Entry a number")
    print (str(int(num1) / int(num2)))
elif operator == '4':
    num1 = input("Entry a number")
    num2 = input("Entry a number")
    print (str(int(num1) * int(num2)))
