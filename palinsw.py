#palindrome swapper
#this program is checking is it possible to construct a palyndrom from a string
strParam='kyaak'
def PalindromeSwapper(strParam):
  length=len(strParam)
  for index, i in enumerate(strParam):
    if index == length-1:
      return -1
    strlist=list(strParam)
    strlist[index], strlist[index+1] = strlist[index+1], strlist[index]
    for letter in strlist:
      strlist=''.join(letter for letter in strlist)
    if strlist == strlist[::-1]:
      return strlist
  strParam=strlist
PalindromeSwapper(strParam)
# keep this function call here
print(PalindromeSwapper(strParam))
