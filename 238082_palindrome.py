string = input("Please input string: ")
string_lower = string.lower()
string_reversed = string_lower[::-1]
if(string_lower == string_reversed):
	print(string, "is a palindrome")
else:
	print(string, "is not a palindrome")