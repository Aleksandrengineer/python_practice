#programm is checking time difference from a list a choosing the least amount in it
strArr=["2:10pm", "1:30pm", "10:30am", "4:42pm"]
import re

def findMinDifference(self, timePoints:) -> 'int':
    n=len(timePoints)
    res=[]
    for i in range(n):
        res.append(int(timePoints[i][0:2])*60+int(timePoints[i][3:5]))
    res.sort()
    tmp=res[0]+24*60-res[n-1]
    for i in range(1,n):
        tmp=min(tmp,res[i]-res[i-1])
    return tmp
print(findMinDifference(timePoints))
