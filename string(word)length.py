#Have the function LongestWord(sen) 
#take the sen parameter being passed and return the longest 
#word in the string. If there are two or more words that are 
#the same length, return the first word from the string with 
#that length. Ignore punctuation and assume sen will not be 
#empty. Words may also contain numbers, 
#for example "Hello world123 567"
def LongestWord(sen):
  lword = ''
  sen = sen.split(' ') #first of all we need to separate word in string
  for word in sen: #taking the separated the word from list of strings
    #print(word)
    clearword = ''
    for letter in word:
      #print(letter)
      if ord(letter) > 65 and ord(letter) < 122: #checking that the word only consists of letter no number or symbols
        #print (letter)
        clearword = clearword+letter #combining letter into a word
        #print(clearword)
    if len(clearword) > len(lword): #checking it length
      lword=clearword
      #print(lword)
  # code goes here
  sen=lword
  return sen
# keep this function call here 
print(LongestWord(input()))