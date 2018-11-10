#  Implement a program to convert the input string to upper case (without using standard library)


def uppercase(string):
    result = ''
    for char in string:
        if ord(char) >= 65:
            result += chr(ord(char) - 32)
    print(result)

def main():
	string=input("Enter any string in Lowercase :")
	uppercase(string)


if __name__ == '__main__':
	main()

