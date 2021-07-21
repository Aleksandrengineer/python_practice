#Given a non-empty list of positive integers l and a target positive integer t, 
# write a function solution(l, t) which verifies if there is at least one consecutive 
# sequence of positive integers within the list l (i.e. a contiguous sub-list) that 
# can be summed up to the given target positive integer t (the key) and returns the 
# lexicographically smallest list containing the smallest start and end indexes where 
# this sequence can be found, or returns the array [-1, -1] in the case that there 
# is no such sequence (to throw off Lambda's spies, not all number broadcasts will 
# contain a coded message).

#For example, given the broadcast list l as [4, 3, 5, 7, 8] and the key t as 12, 
# the function solution(l, t) would return the list [0, 2] because the list l 
# contains the sub-list [4, 3, 5] starting at index 0 and ending at index 2, 
# for which 4 + 3 + 5 = 12, even though there is a shorter sequence that happens 
# later in the list (5 + 7). On the other hand, given the list l as [1, 2, 3, 4] 
# and the key t as 15, the function solution(l, t) would return [-1, -1] because 
# there is no sub-list of list l that can be summed up to the given target value t = 15.
l=[4, 3, 10, 2, 8]
t=1
def solution(l, t):
    sum=0
    count=0
    forcount=0
    length=len(l)
    sol1=list()
    indexcount=0
    #print(length)
    max_val=0
    min_val=0
    sol2=list()
    while sum!=t:
        count=count+forcount
        forcount=0
        #print('count', count)
        if count>=len(l) and l[count-1]!=sum:
            min_val=-1
            max_val=-1
            break
        for index, num in enumerate(l[count:]):
            #print(sum)
            sum=sum+num
            indexcount=index+count
            sol1.append(indexcount)
            if sum==t:
                max_val=max(sol1)
                min_val=min(sol1)
                #sol2.append(min_val)
                #sol2.append(max_val)
                #print(sol1,t)
                break
            elif sum>t:
                forcount=forcount+1
                sol1=list()
                sum=0
                break
    return min_val, max_val
result=solution(l,t)
print(result)