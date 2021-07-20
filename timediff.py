#programm is checking time difference from a list a choosing the least amount in it
import re
strArr=["2:10pm", "1:30pm", "10:30am", "4:42pm"]
def TimeDifference(strArr):
    answ=list()
    diffls=list()
    n=len(strArr)
    for time in strArr:
        pattern='0-9'
        time=time.split(':')
        minutes=time[1]
        minute=re.findall('[0-9]+',minutes)
        minute=int(minute[0])
        hour=time[0]
        hour=int(hour)*60
        times=hour+minute
        answ.append(times)
    #print(answ)
    for i in range(0,n):
        if answ[i]>answ[i-1]:
            diff=answ[i]-answ[i-1]
        else:
            diff=answ[i-1]-answ[i]
            diffls.append(diff)
    #print (diffls)
    strArr=min(diffls)
    return strArr
# keep this function call here 
print(TimeDifference(strArr))
