#There is a broken calculator that has the integer startValue on its display initially.

#In one operation, you can:
#multiply the number on display by 2, or
#subtract 1 from the number on display.
#Given two integers startValue and target, return the minimum number of operations needed to display
#target on the calculator.

#Example 1:
#Input: startValue = 2, target = 3
#Output: 2
#Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

#Example 2:
#Input: startValue = 5, target = 8
#Output: 2
#Explanation: Use decrement and then double {5 -> 4 -> 8}.

#Example 3:
#Input: startValue = 3, target = 10
#Output: 3
#Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.

#Constraints:
#1 <= x, y <= 109
startValue = 5
target = 10
middle_value = startValue
class Solution: #okay the only aproach is to go from the 'target' value to the 'startValue'.

	def operation_1 (target: int): #first i define the first operation
		target = target / 2
		#print('operation_1 ', target) #checking if it is working
		return target

	def operation_2 (target: int): #second i define the second operation
		target = target + 1
		#print('operation_2 ', target) #checking if it is working
		return target

	def brokenCalc(startValue: int, target: int) -> int: #then the main function.
		ans = 0 #this is the calculation of operation that we need to perform to go from 'startValue' to 'target'.
		while target != startValue: #we need a clause to stop loop. 
		#Here it is while the target value (which is changing) is not even to the 'startValue' which is non chaging/
			if target % 2 == 1 or target < startValue: #here we need two clauses. 
			#First is that the leftover from division by 2 is not 0.
			#Second is that the 'target' value is bigger then 'startValue'.
			#As a result in both cases we using the plus operation to get to the even value that can be divided by 2
				ans = ans + 1 #as we perform the operation we need to increse the calculation of operations
				target = Solution.operation_2 (target) #Operation to change the value of 'target'
			else: #if both of that clauses in row 45 is complete, then we divide
				ans = ans + 1 #Operation to change the value of 'target'
				target = Solution.operation_1 (target) #Operation to change the value of 'target'.
		#target = Solution.operation_2 (target) #check inside the calc function
		#print('after operation_2', target) #another check inside the calc function
		#target = target / 2 #another check inside the calc function
		return ans #returning the calculation of the numbers of operations.

print(Solution.brokenCalc (startValue, target)) #calling the function 

