#  Implement a  program to check the elements in the list has word "SOIS"


def count_vowels(str1):
	str1=str1.upper()

	str2=['SOIS']
	for i in str2: 
		if(i==str1):
			print("SOIS is present in input string")
		else:
			print("Not present")

			
	
def main():
	print("To find whether 'SOIS' is present in the input string ")
	str1=input("Enter any string :")
	count_vowels(str1)

if __name__=='__main__':
	main()


	
