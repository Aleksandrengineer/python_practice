# program that prints so it would print only every second letter from code
import string
plain_text=input('Enter the text: ')
if len(plain_text)<1:
    plain_text='abc'
shift_num=input('Enter the cypher value: ')
if len(shift_num)<1:
    shift_num=3
shift_num=int(shift_num)

letters = string.ascii_lowercase #first we create a table with ascii alphabet
#print(letters)
mask = letters[shift_num:] + letters[:shift_num]#then we creating a new table with all characters shifted to the cypher value
#print(mask)
trantab = str.maketrans(letters, mask) #then we are making a connection between both of those: a right table and a shifted one
print(trantab)
print(type(trantab))
#return plain_text.translate(trantab)
plain_text=plain_text.translate(trantab)#here we are asking to type a string for us using the characterictics of the shifted table
print(plain_text)
print(len(plain_text))
