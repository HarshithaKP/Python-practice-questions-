# Implement a program to write a line from the console to a file.

def main():
	f=open("file1.txt","w")
	line=input("Enter a line to add in file :")
	f.write(line)
	

if __name__ == '__main__':
	main()