'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]

'''
def FizzBuzz():
    n=100
    arr=[]
    for i in range(n):
        if (i+1)%5==0 and (i+1)%3==0:
            arr.append("FizzBuzz")
        elif (i+1)%3==0:
            arr.append("Fizz")
        elif (i+1)%5==0:
            arr.append("Buzz")
        else:
            arr.append(str(i+1))
    return arr
print(FizzBuzz())