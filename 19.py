# Implement a program using CLA for simple arithmetic calculator exmaple:
# operand operator operand ie. 10 + 10 / 30 * 20

import sys
import getopt

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
	(myopts,args)=getopt.getopt(sys.argv[1:],"n:p:m:"["number1=","operator=","number2="])
	print("Myopt values :",myopts)
	print("Args values :",args)
	for o,a in myopts:
		
		if o in('-n',"--number1"):
			print("operand1 is ",a)
			n=int(a)
		elif o in('-m',"--number2"):
			print("Opwrand2 is ",a)
			m=int(a)
		elif o in('-p',"--operator"):
			print("Operator is ",a)
			operator=a

	if(operator=='+'):
		addition(num1,num2)
	if(operator=='-'):
		subtraction(num1,num2)
	if(operator=='*'):
		multiplication(num1,num2)
	if(operator=='/'):
		division(num1,num2)

if __name__ == '__main__':
	main()
