
#1-1
print("Hello, world!!!")

#1-2
x = int(input())
h = int(input())
b = int(input())
t = int(input())

total = x + h + b - t
print(total)

#1-3
num = int(input())
sum = 0
for i in range(5):    
    sum += num % 10
    num = int(num/10)
print(sum)    

#2-1
def IsPrimeSmaller(n):
    for i in range(n-1,2,-1):
        if n%i == 0:
            return IsPrimeSmaller(n-1)
    return n        

n = int(input())
n -= 1
print(IsPrimeSmaller(n))

#2-2
def IsPrimeBigger(n):
    for i in range(n-1,2,-1):
        if n%i == 0:
            return IsPrimeBigger(n+1)
    return n

n = int(input())
n += 1
print(IsPrimeBigger(n))

#2-3
def IsEven(n):
    if n%2 == 0:
        print("YES")
    else:
        print("NO")

n = int(input())
IsEven(n)

#3-1 Sorting the Sentence
s = "is2 sentence4 This1 a3"
str = s.split(' ')
for i in range(len(str)):
   str[i] = str[i][-1] + str[i][:-1]
str.sort()

for i in range(len(str)):
    str[i] = str[i][1:]     

print(" ".join(str))


#conflict