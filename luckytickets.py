#this one is checking from a million tickets a lucky tickets only
#Есть 10 рулонов билетов по 100000 штук в каждом (000000-099999, …, 900000-999999),
#  номера которых состоят из 6-ти цифр.
#Надо вычислить у каждого рулона число счастливых билетов.
#Счастливым считается билет, у номера которого среднее 1-2 цифр равно среднему 3-4
#  цифр и равно среднему 5-6 цифр (например: 374655), но при этом все цифры разные
#  (т.е. номер 555555 не считается)
#Желательно чтобы решение было максимально быстрым. При применении формул, нужно
#  объяснить как они работают


letterinnum=list()
luckyticket=dict()
def luckytickets():
    x=0
    roll=0
    while True:
        if x<1000000:
            x=x+100000 #this so i can differ each hundredthousand
            count=0
            roll=roll+1
        else: break
        for num in range(x):
            num=str(num)
            if len(num)<6:
                continue
            else:
                if num[0]+num[1]==num[2]+num[3]: #testing on the same numbers
                   continue
                elif num[0]+num[1]==num[4]+num[5]:
                   continue
                elif num[2]+num[3]==num[4]+num[5]:
                    continue
                else:
                    sumletter=int(num[0])+int(num[1]) 
                    sumletter=sumletter/2 #basically the criteria for luckyticket
                    sumletter1=int(num[2])+int(num[3])
                    sumletter1=sumletter1/2
                    sumletter2=int(num[4])+int(num[5])
                    sumletter2=sumletter2/2
                    if sumletter==sumletter1 and sumletter==sumletter2:
                        letterinnum.append(num)#this gives me all the lucky numbers in list
                        count=count+1
        luckyticket[roll]=count #so i created roll and dict so i could in the end get the number of roll and its number of lucky tickets
        #print(count)
    return letterinnum
luckytickets()
#print(luckyticket) #получается конечный ответ это дикшионари с ки вэлью парой которая обознает номер рулона и кол-во счастливых билетов в нем
for k,v in luckyticket.items():
    print(k,v)