# Implement function to find the string length without using standard library.

def stringlen(str):
	count=0
	for i in str:
		count=count+1
	print("String length if input string is :",count)

def main():
	str=input("Enter any string to find the length:")
	stringlen(str)

if __name__ == '__main__':
	main()