# Implement a function to count the number of vowels present in the file. 

def main():
	f=open("file1.txt","r").read()
	count=0
	for i in f:
		if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
			count=count+1
	print("Total number of vowels :",count)



if __name__ == '__main__':
	main()