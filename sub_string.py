#python pgm to check if a substring is present in a given string
string=input('Enter a string')
substring=input('Enter a substring')
if substring in string:
    print('substring present')
else:
    print('substring not present')
