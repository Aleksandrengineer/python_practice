#the parameter weekday is True if it is a weekday, and the
#parameter vacation is True if we are on vacation. 
#We sleep in if it is not a weekday or we're on vacation
#return True if we sleep in
weekday = input('Is it weekday? ', )
if weekday == 'Yes':
	weekday = True
else:
	weekday = False
#print(weekday)
vacation = input('Is it vacation? ', )
if vacation == 'Yes':
	vacation = True
else:
	vacation = False
#print(vacation)
def sleep_in (weekday, vacation):
	if not weekday==True or vacation==True:
		print('We are sleeping tonight')
		return True
	else:
		print('Go to work you lazyass')
		return False
sleep_in(weekday, vacation)
