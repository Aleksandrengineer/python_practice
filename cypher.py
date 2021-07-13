#changing every letter in a string to another letter which values in user edited value
#a=97, z=122
import string
plain_text=input('Enter the text: ')
shift_num=int(input('Enter the cypher value: '))
letters = string.ascii_lowercase #first we create a table with ascii alphabet
print(letters)
mask = letters[shift_num:] + letters[:shift_num]#then we creating a new table with all characters shifted to the cypher value
print(mask)
trantab = str.maketrans(letters, mask) #then we are making a connection between both of those: a right table and a shifted one
print(trantab)
#return plain_text.translate(trantab)
plain_text=plain_text.translate(trantab)#here we are asking to type a string for us using the characterictics of the shifted table
print(plain_text)
