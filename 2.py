#  Implement a  program  for finding a square of a number.

def square_of_number(num):
	square=num*num
	print("Square of the number is : ",square)
def main():
	print(" Square of number ")
	num=int(input("Enter the number : "))
	square_of_number(num)
if __name__=='__main__':
	main()