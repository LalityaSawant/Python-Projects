numbers = [5,6,7,2,5,7,1,3]
numbers2 = numbers.copy()
numbers3 = numbers

numbers.append(20)
print(numbers)

numbers.insert(1,10)
print(numbers)

numbers.remove(7)
print(numbers)

numbers.pop()
print(numbers)

numbers.index(1)
print(numbers)

print(50 in numbers)

print(numbers.count(5))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(numbers2)
print(numbers3)

numbers.index(50)
print(numbers)

numbers.clear()
print(numbers)