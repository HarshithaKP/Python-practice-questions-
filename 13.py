#  Implment a program with arithmetic functions with  case statements

def addition(num1,num2):
	summ=num1+num2
	print(summ)
	#print("Addition of numbers is :",summ)
def subtraction(num1,num2):
	diff=num1-num2
	print(diff)
	#print("Difference between numbers is: ",diff)
def multiplication(num1,num2):
	mul=num1*num2
	print("Product of numbers is: ",mul)
def division(num1,num2):
	div=num1/num2
	print("Quotient after division is: ",div)

def switchfun(option,num1,num2):
	
	switch={
			'+': addition(num1,num2),
			'-': subtraction(num1,num2),
			'*': multiplication(num1,num2),
			'/': division(num1,num2),
	}
	print( "Answer is", switch.get(option) )
	

def main():
	while True:
		num1=float(input("Enter first number :"))
		num2=float(input("Enter second number :"))
		print("+: Addition")
		print("-: Subtraction")
		print("*: Multiplication")
		print("/: Division")
		option=input("Enter your option :")
		switchfun(option,num1,num2)

if __name__ == '__main__':
	main()
