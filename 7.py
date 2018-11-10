#Implement a program to reverse a string (without standard library function)

def reverse_string(string):
	newstr=' '
	for i in string:
		newstr=i+newstr
	print("Originsal string :",string)
	print("Reversed string :",newstr)
def main():
	string=input("Enter the string to be reversed :" )
	reverse_string(string)
if __name__ == '__main__':
	main()