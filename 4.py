#  Implement a  program to check the count of vowels in a given string.(with repeated occurance)

def count_vowels(str1):
	count=0
	str2=['a','e','i','o','u']
	for i in str1:
		if(i in str2):
			count+=1
	print("Total number of vowels in the given string are :",count)

def main():
	str1=input("Enter any string :")
	count_vowels(str1)

if __name__=='__main__':
	main()


	
