#List:- List is a collection which is ordered and changeable. 
# Allows duplicate members.
# Lists are used to store multiple items in a single variable.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# List is a mutable.
# List allows heterogenous values.
# List is denoted by [].
# Negative indexing is also possible.


# my_list=[1,2,1,True,"virat"]
# print(my_list)
# my_list[2]="pine apple"
# print(my_list)
# print(len(my_list))
# print(my_list[4])
# print(my_list[2:5])
# print(my_list[:4])
# print(my_list[0:])

# my_list1=list(("apple","banana","cherry"))
# print(type(my_list1))
# print(my_list1)

# List Methods:

# 1.append() :Adds an element at the end of the list
# 2.clear()  :Removes all the elements from the list
# 3.copy()   :Returns a copy of the list
# 4.count()  :Returns the number of elements with the specified value
# 5.extend() :Add the elements of a list (or any iterable), to the end of the current list
# 6.index()  :Returns the index of the first element with the specified value
# 7.insert() :Adds an element at the specified position
# 8.pop()    :Removes the element at the specified position
# 9.remove() :Removes the item with the specified value
# 10.reverse():Reverses the order of the list
# 11.sort()   :Sorts the list

#1.append()

# my_list=["apple","banana","mango"]
# # my_list.append("guava")
# # print(my_list)
# cars=["Ford","BMW","skoda"]
# my_list.append(cars)
# print(my_list)

#2.clear()

# cars=["Ford","BMW","skoda"]
# cars.clear()
# print(cars)

#3.copy()

# fruits=["Apple","Banana","Mango","Kiwi","Orange"]
# print(fruits)
# x=fruits.copy()
# print(x)

#4.count()

# list=[1,3,2,4,4,6,5,4,7,8,8,9,4]
# l2=list.count(4)
# print(l2)

# fruits = ["apple", "banana", "cherry"]
# x = fruits.count("cherry")
# print(x)

#5.extend()

# fruits=["Apple","Banana","Kiwi","Mango"]
# print(fruits)
# points=[1,2,3,4]
# fruits.extend(points)
# print(fruits)

#6.index()

# fruits=["Apple","Banana","Kiwi","Mango"]
# x=fruits.index('Mango')
# print(x)

# fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
# x = fruits.index("cherry", 4)
# print(x)

#7.insert()

# cars=['Ford','Duster','Fortuner','Enova','Curvev']
# cars.insert(2,'Range Rover')
# print(cars)

#8.pop()

# fruits=['Apple','Banana','Watermelon','Mango']
# # x=fruits.pop()
# x=fruits.pop(1)
# print(x)

#9.remove()

# fruits=['Apple','Banana','Mango','Cherry']
# fruits.remove('Apple')
# print(fruits)

#10.reverse()

# fruits = ['apple', 'banana', 'cherry','Mango']
# fruits.reverse()
# print(fruits)

# numbers=[1,3,5,6,7,8,9,4,2,1,2,3,5]
# numbers.reverse()
# print(numbers)

#11.sort()

# cars=['Hummer','Volvo','BMW','Ford']
# cars.sort()
# print(cars)

# cars=['Hummer','Volvo','BMW','Ford']
# cars.sort(reverse=True)
# print(cars)


# def myFunc(e):
#     return len(e)

# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
# cars.sort(key=myFunc)

# print(cars)


# def myfunc(e):
#     return e['year']

# cars = [
#   {'car': 'Ford', 'year': 2005},
#   {'car': 'Mitsubishi', 'year': 2000},
#   {'car': 'BMW', 'year': 2019},
#   {'car': 'VW', 'year': 2011}
# ]

# cars.sort(key=myfunc)
# print(cars)


# def myfunc(e):
#     return len(e)

# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

# cars.sort(reverse=True, key=myfunc)
# print(cars)
