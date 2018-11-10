# Implement a program using CLA for simple arithmetic calculator exmaple:
# operand operator operand ie. 10 + 10 / 30 * 20

import sys
def addition(num1,num2):
	summ=num1+num2
	print("Sum of two numbers is :",summ)

def subtraction(num1,num2):
	subt=num1-num2
	print("Sum of two numbers is :",subt)


def multiplication(num1,num2):
	mul=num1*num2
	print("Sum of two numbers is :",mul)

def divisionion(num1,num2):
	div=num1/num2
	print("Sum of two numbers is :",div)

def main():
	print("program using CLA for simple arithmetic calculator")
	try:
		num1=int(sys.argv[1])
		num2=int(sys.argv[3])
		operand=sys.argv[2]

		if(operand=='+'):
			addition(num1,num2)
		if(operand=='-'):
			subtraction(num1,num2)
		if(operand=='*'):
			multiplication(num1,num2)
		if(operand=='/'):
			division(num1,num2)
	except Exception as e:
		print("Usage <name.py> num1 operand num2 (operand:+,-,*,/)")
	
	finally:
		sys.exit()
	

if __name__ == '__main__':
	main()