weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
sum = 0
max = 0
for index in range (len(weights)):
    sum += weights[index]
    if max < weights[index]:
        max = weights[index]

aver_weights = int(sum/days)
if aver_weights > max:
    capacity = aver_weights
else:
    capacity = max

def CapacityCalculator(weights, capacity, days):
    counter = 0
    index = 0
    while index < len(weights):
        sum = 0
        while sum < capacity:
            sum += weights[index] 
            if sum == capacity:
                counter += 1
                index += 1
                sum = 0
            elif sum > capacity:
                counter += 1
                sum = 0
            else:
                if index == len(weights) - 1:
                    counter += 1
                else:
                    index += 1        
    if counter > days:
        return CapacityCalculator(weights, capacity + 1, days)
    else:
        return capacity    

print(CapacityCalculator(weights, capacity, days))
