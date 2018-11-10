# Implement a menu based  program for Arithemetic Calculator

import sys
def addition(num1,num2):
	summ=num1+num2;
	print("Sum of two numbers is :",summ);

def subtraction(num1,num2):
	diff=num1-num2;
	print("Diffetence of two numbers is :",diff);

def multiplication(num1,num2):
	mul=num1*num2;
	print("Multiplication of two numbers is :",mul);

def division(num1,num2):
	div=num1/num2;
	print("Division of two numbers is :",div);

def modulus(num1,num2):
	mod=num1%num2;
	print("Remainder is :",mod);

def main():
	print("Simple Arithemetic calculatior ")
	while True:
		num1=int(input("Enter the first number :"));
		num2=int(input("Enter the second number :"));

		print("1 : Addition ")
		print("2 : Subtraction ")
		print("3 : Multiplication ")
		print("4 : Division ")
		print("5 : Remainder ")
		print("q : Quit ")
		
		option=input("Choose the operation to perform : ")
		if(option=='1'):
			addition(num1,num2)
		elif(option=='2'):
			subtraction(num1,num2)
		elif(option=='3'):
			multiplication(num1,num2)
		elif(option=='4'):
			division(num1,num2)
		elif(option=='5'):
			modulus(num1,num2)
		elif(option=='q'):
			sys.exit()
		else:
			print("Enter the correct option !")

if __name__ == '__main__':
	main()



