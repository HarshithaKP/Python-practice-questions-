#  Implement a program to read alternative characters in the file.


def main():
	f=open("file1.txt","r").read()
	print(f[0:10:2])

if __name__ == '__main__':
	main()