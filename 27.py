#  Implement a progam to convert the input string to lower case ( without using standard library)

def lowercase(string):
    result = ''
    for char in string:
        if ord(char) <=90:
            result += chr(ord(char) + 32)
    print(result)

def main():
	string=input("Enter any string in uppercase :")
	lowercase(string)


if __name__ == '__main__':
	main()
