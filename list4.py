numbers = [12, 45, 75, 86, 59, 30, 75, 82, 37]
numbers.append(100)
print(numbers)


#insert
numbers = [12, 45, 75, 86, 59, 30, 75, 82, 37]
numbers.insert(0,100)
print(numbers)

#remove
numbers = [12, 45, 75, 86, 59, 30, 75, 82, 37]
numbers.remove(45)
print(numbers)

#to clear a list
numbers = [12, 45, 75, 86, 59, 30, 75, 82, 37]
numbers.clear()
print(numbers)


#last item remove
numbers = [12, 45, 75, 86, 59, 30, 75, 82, 37]
numbers.pop()
print(numbers)

#index to chea the existence of a number in a list
numbers = [12, 45, 75, 86, 59, 30, 75, 82, 37]
print(numbers.index(59))


numbers = [12, 45, 75, 86, 59, 30, 75, 82, 37]
print(50 in numbers)

#count the times a number appears in a list
numbers = [12, 45, 75, 86, 59, 30, 75, 82, 37]
print(numbers.count(45))

#to order the list in asending order
numbers = [12, 45, 75, 86, 59, 30, 75, 82, 37]
numbers.sort()
print(numbers)

numbers = [12, 45, 75, 86, 59, 30, 75, 82, 37]
numbers.sort()
numbers.reverse()
print(numbers)


#to coppy the original list
numbers = [12, 45, 75, 86, 59, 30, 75, 82, 37]
numbers1 = numbers.copy()
numbers.append(17)
print(numbers1)
