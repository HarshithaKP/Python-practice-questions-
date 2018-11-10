# Implement a program to get three values from CLA and print the sum of them.

import sys
def cla_sum():
	summ=0
	a=int(sys.argv[1])
	b=int(sys.argv[2])
	c=int(sys.argv[3])
	summ=summ+a+b+c
	print("Sum of 3 numbers is :",summ)
def main():
	print("program to get three values from CLA and print the sum of them")
	try:
		cla_sum()

	except Exception as e:
		print(" Usage <name.py> num1 num2 num3")
	
	finally:
		sys.exit()

if __name__ == '__main__':
	main()