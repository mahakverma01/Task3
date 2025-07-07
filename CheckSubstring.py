# Check if one string is a substring of another

string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")

if substring in string:
    print(f'"{substring}" is a substring of "{string}".')
else:
    print(f'"{substring}" is NOT a substring of "{string}".')