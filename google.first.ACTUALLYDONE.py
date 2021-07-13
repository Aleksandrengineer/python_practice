#donot quite remember what it is doing, but it is from the first task from google foobar
#Input: solution.solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])
#second input
#input=([13, 5, 6, 2, 5], [5, 2, 5, 13])#test
#x=input[0]#test
#y=input[1]#test
def solution(x,y):
    for num in x:
        if num not in y:
            misid=num
            #print(misid)
    for num  in y:
        if num not in x:
            misid=num
            #print(misid)
    return misid
#misid=solution(x,y)#test
#print(misid)#test
