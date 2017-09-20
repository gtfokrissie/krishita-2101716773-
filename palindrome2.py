string = input("Please input string: ")
string_lower = string.lower()
string_reversed = string_lower[::-1]
while(string_lower!=string_reversed):
	print(string, "is not a palindrome")
	string = input("Please input string: ")
	string_lower = string.lower()
	string_reversed = string_lower[::-1]
print(string, "is a palindrome")
